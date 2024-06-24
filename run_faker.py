from test_faker import *


@pytest.mark.smoke
def test_username_press(page: Page, username_press):
    username_press()


@pytest.mark.smoke
def test_textarea(page: Page, textarea):
    textarea()


@pytest.mark.smoke
def test_set_filename(page: Page, set_filename):
    set_filename()


@pytest.mark.smoke
def test_username_pressmim(page: Page, username_pressmim):
    username_pressmim()


@pytest.mark.smoke
def test_textareamim(page: Page, textareamim):
    textareamim()


@pytest.mark.smoke
def test_set_filenamemim(page: Page, set_filenamemim):
    set_filenamemim()


@pytest.mark.smoke
def test_username_pressfactory(page: Page, username_pressfactory):
    username_pressfactory()


@pytest.mark.smoke
def test_textareafactory(page: Page, textareafactory):
    textareafactory()


@pytest.mark.smoke
def test_set_filenamefactory(page: Page, set_filenamefactory):
    set_filenamefactory()


@pytest.mark.smoke
def test_username_presshyp(page: Page, username_presshyp):
    username_presshyp()


@pytest.mark.smoke
def test_textareahyp(page: Page, textareahyp):
    textareahyp()


@pytest.mark.smoke
def test_set_filenamehyp(page: Page, set_filenamehyp):
    set_filenamehyp()
