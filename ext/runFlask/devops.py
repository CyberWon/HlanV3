from flask import Blueprint, render_template,request
from hlan import hlan,conf
devops_index=Blueprint('devops_index',__name__,template_folder='/templates')
@devops_index.route('/devops')
def DevOpsIndex():
    return render_template('devops/index.html')