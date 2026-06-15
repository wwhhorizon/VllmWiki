# vllm-project/vllm#14884: [Bug]: if chat_template loaded from disk, jinja exception thrown from _try_extract_ast()

| 字段 | 值 |
| --- | --- |
| Issue | [#14884](https://github.com/vllm-project/vllm/issues/14884) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: if chat_template loaded from disk, jinja exception thrown from _try_extract_ast()

### Issue 正文摘录

### 🐛 Describe the bug When a chat template (which contains at least one "\n" substring) is loaded from disk with `--chat-template` (probably also in the case it's provided in the request), then an exception is thrown from the flow that tries to detect the chat template content format: ``` ERROR 03-16 13:00:42 chat_utils.py:275] Error when compiling Jinja template ERROR 03-16 13:00:42 chat_utils.py:275] Traceback (most recent call last): ERROR 03-16 13:00:42 chat_utils.py:275] File "/home/user/code/debug/.venv/lib/python3.10/site-packages/vllm/entrypoints/chat_utils.py", line 271, in _try_extract_ast ERROR 03-16 13:00:42 chat_utils.py:275] jinja_compiled = hf_chat_utils._compile_jinja_template(chat_template) ERROR 03-16 13:00:42 chat_utils.py:275] File "/home/user/code/debug/.venv/lib/python3.10/site-packages/transformers/utils/chat_template_utils.py", line 435, in _compile_jinja_template ERROR 03-16 13:00:42 chat_utils.py:275] return jinja_env.from_string(chat_template) ERROR 03-16 13:00:42 chat_utils.py:275] File "/home/user/code/debug/.venv/lib/python3.10/site-packages/jinja2/environment.py", line 1108, in from_string ERROR 03-16 13:00:42 chat_utils.py:275] return cls.from_code...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: n is thrown from the flow that tries to detect the chat template content format: ``` ERROR 03-16 13:00:42 chat_utils.py:275] Error when compiling Jinja template ERROR 03-16 13:00:42 chat_utils.py:275] Traceback (most re...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 1, in _try_extract_ast ERROR 03-16 13:00:42 chat_utils.py:275] jinja_compiled = hf_chat_utils._compile_jinja_template(chat_template) ERROR 03-16 13:00:42 chat_utils.py:275] File "/home/user/code/debug/.venv/lib/python3....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: jinja2.exceptions.TemplateSyntaxError: expected token 'end of statement block', got 'name' INFO 03-16 13:00:42 chat_utils.py:338] Detected the chat template content format to be 'string'. You can set `--chat-template-co...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: k with `--chat-template` (probably also in the case it's provided in the request), then an exception is thrown from the flow that tries to detect the chat template content format: ``` ERROR 03-16 13:00:42 chat_utils.py:...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: mething that was never escaped, and it breaks the template content. Can reproduce the `decode()` issue standalone by creating a file with the contents: "foo \n bar" (actually write "\n", not a real newline). then try th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
