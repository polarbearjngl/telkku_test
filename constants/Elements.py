class Elements(object):

    # Main Screen
    NAVIGATION_MENU_BUTTON = 'Open navigation drawer'  # accessibility_id

    # Main Menu
    MAIN_MENU = 'androidx.appcompat.widget.LinearLayoutCompat'  # class
    TV_OHJELMAT_MENU_ITEM = '//androidx.appcompat.widget.LinearLayoutCompat[1]'
    ELOKUVAT_MENU_ITEM = '//androidx.appcompat.widget.LinearLayoutCompat[2]'

    # Movie List
    TOOLBAR_TITLE = '//android.widget.LinearLayout/android.view.View/android.widget.TextView'  # xpath
    DATE_SELECTOR = 'fi.almamedia.telkkucom.staging:id/action_toggle_date_selector'  # id
    MOVIE_ELEMENT = '//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[{n}]'
    MOVIE_MAIN_IMAGE = MOVIE_ELEMENT + '/android.view.ViewGroup/android.widget.ImageView[{1}]'
    MOVIE_CHANNEL_IMAGE = MOVIE_ELEMENT + '/android.view.ViewGroup/android.widget.ImageView[{2}]'
    MOVIE_TITLE = MOVIE_ELEMENT + '/android.view.View/android.widget.TextView[1]'
    MOVIE_TIME = MOVIE_ELEMENT + '/android.view.View/android.widget.TextView[2]'
    MOVIE_IMDB_RATE = MOVIE_ELEMENT + '/android.view.View/android.widget.TextView[3]'
    MOVIE_DESCRIPTION = MOVIE_ELEMENT + '/android.view.View/android.widget.TextView[4]'
