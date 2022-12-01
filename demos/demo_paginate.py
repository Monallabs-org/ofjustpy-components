"""
drop down color not working in firefox
"""

from py_tailwind_utils import *
import ofjustpy as oj
from addict_tracking_changes import Dict
import justpy as jp
import ofjustpy_components as ojx
import itertools

def on_btn_click(dbref,msg):
    pass

app = jp.build_app()
def chunks(iterable, size):
    """Generate adjacent chunks of data"""
    it = iter(iterable)
    return iter(lambda: tuple(itertools.islice(it, size)), ())

def launcher(request):
    session_manager = oj.get_session_manager(request.session_id)
    with oj.sessionctx(session_manager):
        items = [oj.Span_(f"item_{i}", text=f"item {i}") for i in range(16 * 100)]
        paginate_ = ojx.Paginate_("mypaginate", cgens = items, num_pages=16)
        wp_ = oj.WebPage_("oa",
                          cgens =[paginate_],
                          template_file='svelte.html',
                          title="myoa")
        wp = wp_()
        #oj.get_svelte_safelist(session_manager.stubStore)
    return wp

app.add_jproute("/", launcher)

