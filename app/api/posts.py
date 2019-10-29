from app.api import bp

@bp.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    pass

@bp.route('/users', methods=['GET'])
def get_posts():
    pass


@bp.route('/posts', methods=['POST'])
def create_post():
    pass
