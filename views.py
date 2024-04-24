from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session

views = Blueprint(__name__, 'views')

usernames = ['tim', 'joe', 'bill', 'amaan']

@views.route('/')
def home():
    return render_template('index.html', name = "tim", age= 21)


@views.route('/profile')
def profile():
    args = request.args
    username = args.get('username')
    if username in usernames:
        return render_template('index.html', name = username)
    else:
        return "User not found!"
    
@views.route('/json')
def get_json():
    return jsonify({"name": "tim", "age": 21})

@views.route("/gotohome")
def gotohome():
    return redirect(url_for('views.home'))

@views.route('/gallery')
def gallery():
    media_files = session.get('media_files', [])
    return render_template('gallery.html', media_files=media_files)

@views.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form.get('query')
        # ... your search code here ...
        media_files = [
            {'type': 'video', 'src': 'Penalty.mp4'},
            {'type': 'video', 'src': 'v_WallPushups_g11_c03.mp4'},
            {'type': 'video', 'src': 'v_WallPushups_g19_c03.mp4'},
            {'type': 'video', 'src': 'v_WallPushups_g20_c03.mp4'},
            {'type': 'video', 'src': 'v_WallPushups_g20_c03.mp4'},
            {'type': 'video', 'src': 'v_WallPushups_g20_c03.mp4'},
            {'type': 'video', 'src': 'v_WallPushups_g20_c03.mp4'},
            {'type': 'video', 'src': 'v_WallPushups_g20_c03.mp4'},
            {'type': 'video', 'src': 'v_WallPushups_g23_c01.mp4'}
        ]
        session['media_files'] = media_files
        return redirect(url_for('views.gallery'))
    return render_template('search.html')