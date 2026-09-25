import pytest
from playwright.sync_api import BrowserContext


# Hook của pytest để kiểm tra xem test case có bị FAILED hay không
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


# Fixture tự động bật ghi Trace và chỉ lưu khi test rớt
@pytest.fixture(autouse=True)
def auto_trace_and_screenshot_on_failure(context: BrowserContext, request):
    # 1. Bắt đầu ghi lại toàn bộ thao tác, ảnh chụp, snapshot mạng
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield  # Chờ cho test case thực thi xong

    # 2. Kiểm tra nếu test case bị FAIL thì lưu file trace.zip
    node = request.node
    if hasattr(node, "rep_call") and node.rep_call.failed:
        trace_path = f"traces/{node.name}.zip"
        context.tracing.stop(path=trace_path)
    else:
        context.tracing.stop()