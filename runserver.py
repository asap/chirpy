# -*- coding: utf-8 -*-

from chirpy import app as application


if __name__ == '__main__':
    application.run(debug=application.config.get('DEBUG'),
                    use_reloader=application.config.get('USE_RELOADER'))