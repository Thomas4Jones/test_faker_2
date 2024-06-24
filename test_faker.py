import pytest
from playwright.sync_api import sync_playwright, Page, BrowserContext
from data_faker import *
from locator import *


@pytest.fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture
def browser(get_playwright):
    browser = get_playwright.chromium.launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture
def browser_context(browser):
    context = browser.new_context(accept_downloads=True)
    yield context
    context.close()


@pytest.fixture
def page(browser_context: BrowserContext):
    page = browser_context.new_page()
    yield page
    page.close()


@pytest.fixture
def username_press(page: Page):
    def username_press_func():
        test_data = generate_test_data_faker()
        page.goto(data_page_form_example)
        page.wait_for_timeout(1000)
        page.locator(locator_username).fill(test_data["name"])
        page.locator(locator_password).fill(test_data["password"])
        page.wait_for_timeout(1000)
        page.click(locator_submit)
        page.wait_for_timeout(1000)
        page.screenshot(path='screen_faker/username.png')
    return username_press_func


@pytest.fixture
def textarea(page: Page):
    def textarea_func():
        test_data = generate_test_data_faker()
        page.goto(data_page_form_example)
        page.wait_for_timeout(1000)

        def key_textarea(locator_textarea: str, test_data: str):
            page.click(locator_textarea)
            page.keyboard.down("Shift")
            for _ in range(8):
                page.keyboard.press("ArrowLeft")
            page.keyboard.up("Shift")
            page.keyboard.type(test_data)
        key_textarea(locator_textarea, test_data["text"])
        page.wait_for_timeout(1000)
        page.screenshot(path='screen_faker/textarea.png')
        page.click(locator_submit)
        page.screenshot(path='screen_faker/textarea2.png')
    return textarea_func


@pytest.fixture
def set_filename(page: Page):
    def set_filename_func():
        file_content = fake.text(max_nb_chars=1000)
        with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix=".txt") as temp_file:
            temp_file.write(file_content)
            temp_file_path = temp_file.name
        page.goto(data_page_form_example)
        page.wait_for_timeout(1000)
        page.click(locator_filename)
        page.set_input_files('input[type="file"]', temp_file_path)
        page.wait_for_timeout(2000)
        page.screenshot(path="screen_faker/set_filename.png")
        page.click(locator_submit)
        page.wait_for_timeout(2000)
        expected_filename = os.path.basename(temp_file_path)
        assert expected_filename == page.locator(locator_filename_2).inner_text()
        page.screenshot(path="screen_faker/set_filename2.png")
        os.remove(temp_file_path)
    return set_filename_func


@pytest.fixture
def username_pressmim(page: Page):
    def username_pressmim_func():
        test_data = generate_test_data_mimesis()
        page.goto(data_page_form_example)
        page.wait_for_timeout(1000)
        page.locator(locator_username).fill(test_data["name"])
        page.locator(locator_password).fill(test_data["password"])
        page.wait_for_timeout(1000)
        page.click(locator_submit)
        page.wait_for_timeout(1000)
        page.screenshot(path='screen_mimesis/username.png')
    return username_pressmim_func


@pytest.fixture
def textareamim(page: Page):
    def textareamim_func():
        test_data = generate_test_data_mimesis()
        page.goto(data_page_form_example)
        page.wait_for_timeout(1000)

        def key_textarea(locator_textarea: str, data_textarea: str):
            page.click(locator_textarea)
            page.keyboard.down("Shift")
            for _ in range(8):
                page.keyboard.press("ArrowLeft")
            page.keyboard.up("Shift")
            page.keyboard.type(data_textarea)
        key_textarea(locator_textarea, test_data["text"])
        page.wait_for_timeout(1000)
        page.screenshot(path='screen_mimesis/textarea.png')
        page.click(locator_submit)
        page.screenshot(path='screen_mimesis/textarea2.png')
    return textareamim_func


@pytest.fixture
def set_filenamemim(page: Page):
    def set_filenamemim_func():
        text_generator = Text(locale=Locale.RU, seed=42)
        file_content = text_generator.text()
        with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix=".txt") as temp_file:
            temp_file.write(file_content)
            temp_file_path = temp_file.name
        page.goto(data_page_form_example)
        page.wait_for_timeout(1000)
        page.click(locator_filename)
        page.set_input_files('input[type="file"]', temp_file_path)
        page.wait_for_timeout(2000)
        page.screenshot(path="screen_mimesis/set_filename.png")
        page.click(locator_submit)
        page.wait_for_timeout(2000)
        expected_filename = os.path.basename(temp_file_path)
        assert expected_filename == page.locator(locator_filename_2).inner_text()
        page.screenshot(path="screen_mimesis/set_filename2.png")
        os.remove(temp_file_path)
    return set_filenamemim_func


@pytest.fixture
def username_pressfactory(page: Page):
    def username_pressfactory_func():
        test_data = UserFactory.build()
        page.goto(data_page_form_example)
        page.wait_for_timeout(1000)
        page.locator(locator_username).fill(test_data["name"])
        page.locator(locator_password).fill(test_data["password"])
        page.wait_for_timeout(1000)
        page.click(locator_submit)
        page.wait_for_timeout(1000)
        page.screenshot(path='screen_factory/username.png')
    return username_pressfactory_func


@pytest.fixture
def textareafactory(page: Page):
    def textareafactory_func():
        test_data = UserFactory.build()
        page.goto(data_page_form_example)
        page.wait_for_timeout(1000)

        def key_textarea(locator_textarea: str, data_textarea: str):
            page.click(locator_textarea)
            page.keyboard.down("Shift")
            for _ in range(8):
                page.keyboard.press("ArrowLeft")
            page.keyboard.up("Shift")
            page.keyboard.type(data_textarea)
        key_textarea(locator_textarea, test_data["text"])
        page.wait_for_timeout(1000)
        page.screenshot(path='screen_factory/textarea.png')
        page.click(locator_submit)
        page.screenshot(path='screen_factory/textarea2.png')
    return textareafactory_func


@pytest.fixture
def set_filenamefactory(page: Page):
    def set_filenamefactory_func():
        #file_content = UserFactory.facker.text(max_nb_chars=1000)
        file_content = 'test_file_content'
        with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix=".txt") as temp_file:
            temp_file.write(file_content)
            temp_file_path = temp_file.name
        page.goto(data_page_form_example)
        page.wait_for_timeout(1000)
        page.click(locator_filename)
        page.set_input_files('input[type="file"]', temp_file_path)
        page.wait_for_timeout(2000)
        page.screenshot(path="screen_factory/set_filename.png")
        page.click(locator_submit)
        page.wait_for_timeout(2000)
        expected_filename = os.path.basename(temp_file_path)
        assert expected_filename == page.locator(locator_filename_2).inner_text()
        page.screenshot(path="screen_factory/set_filename2.png")
        os.remove(temp_file_path)
    return set_filenamefactory_func


@pytest.fixture
def username_presshyp(page: Page):
    def username_presshyp_func():
        test_data = generate_test_data_hypothesis()
        page.goto(data_page_form_example)
        page.wait_for_timeout(1000)
        page.locator(locator_username).fill(test_data["name"])
        page.locator(locator_password).fill(test_data["password"])
        page.wait_for_timeout(1000)
        page.click(locator_submit)
        page.wait_for_timeout(1000)
        page.screenshot(path='screen_hypothesis/username.png')
    return username_presshyp_func


@pytest.fixture
def textareahyp(page: Page):
    def textareahyp_func():
        test_data = generate_test_data_hypothesis()
        page.goto(data_page_form_example)
        page.wait_for_timeout(1000)

        def key_textarea(locator_textarea: str, data_textarea: str):
            page.click(locator_textarea)
            page.keyboard.down("Shift")
            for _ in range(8):
                page.keyboard.press("ArrowLeft")
            page.keyboard.up("Shift")
            page.keyboard.type(data_textarea)
        key_textarea(locator_textarea, test_data["text"])
        page.wait_for_timeout(1000)
        page.screenshot(path='screen_hypothesis/textarea.png')
        page.click(locator_submit)
        page.screenshot(path='screen_hypothesis/textarea2.png')
    return textareahyp_func


@pytest.fixture
def set_filenamehyp(page: Page):
    def set_filenamehyp_func():
        def file_content_strategy(draw):
            return draw(st.text(min_size=1, max_size=1000))
        file_content = file_content_strategy(draw=50)
        with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix=".txt") as temp_file:
            temp_file.write(file_content.example())
            temp_file_path = temp_file.name
        page.goto(data_page_form_example)
        page.wait_for_timeout(1000)
        page.click(locator_filename)
        page.set_input_files('input[type="file"]', temp_file_path)
        page.wait_for_timeout(2000)
        page.screenshot(path="screen_hypothesis/set_filename.png")
        page.click(locator_submit)
        page.wait_for_timeout(2000)
        expected_filename = os.path.basename(temp_file_path)
        assert expected_filename == page.locator(locator_filename_2).inner_text()
        page.screenshot(path="screen_hypothesis/set_filename2.png")
        os.remove(temp_file_path)
    return set_filenamehyp_func
