from flask import Flask, flash, request, render_template, session, redirect
from flask_debugtoolbar import DebugToolbarExtension
import requests 


class Convert():

    def convert():
        '''Retreives API and form data, calculates result'''
        try:
            url = 'https://api.exchangerate.host/latest'
            response = requests.get(url)
            data = response.json()
            currlist = data['rates'].keys()
            incurr = request.form['incurr'].upper()
            outcurr = request.form['outcurr'].upper()
            inval = request.form['inval'].replace(',','')
            if f'{incurr}' not in currlist or f'{outcurr}' not in currlist:
                flash('INVALID CURRENCY', 'warning')
                return redirect('/')
            elif not inval.replace('.','',1).isdigit():
                flash('INVALID NUMBER', 'warning')
                return redirect('/')
            else:
                outval = round((float(inval) * float(data['rates'][outcurr]) / float(data['rates'][incurr])), 4)
                return render_template("result.html",
                                outval=outval,
                                inval=inval,
                                incurr=incurr,
                                outcurr=outcurr)
        except Exception as e:
            return redirect('/')