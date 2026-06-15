# vllm-project/vllm#23744: [Bug]: from vllm import LLM works but vllm serve raises OSError('source code not available')

| 字段 | 值 |
| --- | --- |
| Issue | [#23744](https://github.com/vllm-project/vllm/issues/23744) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: from vllm import LLM works but vllm serve raises OSError('source code not available')

### Issue 正文摘录

### Your current environment collect_env.py same crash. Ubuntu 24.04 with system python 3.12 UV venv with 3.12 works but crashes later while 3.13 give this error ### 🐛 Describe the bug ``` vllm serve ./tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf --tokenizer TinyLlama/TinyLlama-1.1B-Chat-v1.0wget https://raw.githubusercontent.com/vllm-project/vllm/main/vllm/collect_env.py # For security purposes, please feel free to check the contents of collect_env.py before running it. python collect_env.py INFO 08-27 14:10:13 [__init__.py:241] Automatically detected platform cuda. Traceback (most recent call last): File "/home/usr/.local/share/uv/python/cpython-3.13.4-linux-x86_64-gnu/lib/python3.13/inspect.py", line 1087, in findsource lnum = vars(object)['__firstlineno__'] - 1 ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^ KeyError: '__firstlineno__' During handling of the above exception, another exception occurred: Traceback (most recent call last): File "/home/usr/llm/.venv/bin/vllm", line 10, in sys.exit(main()) ~~~~^^ File "/home/usr/llm/.venv/lib/python3.13/site-packages/vllm/entrypoints/cli/main.py", line 46, in main cmd.subparser_init(subparsers).set_defaults( ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^ File "/home/usr/...

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: from vllm import LLM works but vllm serve raises OSError('source code not available') bug;stale ### Your current environment collect_env.py same crash. Ubuntu 24.04 with system python 3.12 UV venv with 3.12 works...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: py INFO 08-27 14:10:13 [__init__.py:241] Automatically detected platform cuda. Traceback (most recent call last): File "/home/usr/.local/share/uv/python/cpython-3.13.4-linux-x86_64-gnu/lib/python3.13/inspect.py", line 1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: while 3.13 give this error ### 🐛 Describe the bug ``` vllm serve ./tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf --tokenizer TinyLlama/TinyLlama-1.1B-Chat-v1.0wget https://raw.githubusercontent.com/vllm-project/vllm/main/vllm/co...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nt frontend_api;model_support cuda crash env_dependency #23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: LLM works but vllm serve raises OSError('source code not available') bug;stale ### Your current environment collect_env.py same crash. Ubuntu 24.04 with system python 3.12 UV venv with 3.12 works but crashes later while...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23752: Should have ROCm label: NO (0 matches) #23744: Should have ROCm label: NO (0 matches) #23739: Should have ROCm label: NO (0 matches) #23730: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
