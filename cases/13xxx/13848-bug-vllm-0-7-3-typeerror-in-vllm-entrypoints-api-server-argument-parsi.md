# vllm-project/vllm#13848: [Bug]: vLLM 0.7.3 TypeError in vllm.entrypoints.api_server Argument Parsing

| 字段 | 值 |
| --- | --- |
| Issue | [#13848](https://github.com/vllm-project/vllm/issues/13848) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM 0.7.3 TypeError in vllm.entrypoints.api_server Argument Parsing

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running vllm.entrypoints.api_server, I encounter a TypeError related to argparse argument parsing. ```bash poetry run python -m vllm.entrypoints.api_server \ --model SomeOrg/SomeModel \ --host 0.0.0.0 \ --port 8000 ``` **Error Message** ```bash Traceback (most recent call last): File "/path/to/python3.11/runpy.py", line 196, in _run_module_as_main return _run_code(code, main_globals, None, File "/path/to/python3.11/runpy.py", line 86, in _run_code exec(code, run_globals) File "/path/to/vllm/entrypoints/api_server.py", line 148, in parser.add_argument("--port", type=int, default=8000, ge=1024, le=65535) File "/path/to/python3.11/argparse.py", line 1430, in add_argument action = action_class(**kwargs) TypeError: _StoreAction.__init__() got an unexpected keyword argument 'ge' ``` **Steps to Reproduce** 1. Install vLLM from source using: ```bash git clone https://github.com/vllm-project/vllm.git cd vllm pip install . ``` 2. Run the vLLM API Server command as shown above. 3. Observe the TypeError due to the `ge` argument **Expected Behavior** The API server should start normally, listening on the specified port. **Additional Debu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: got an unexpected keyword argument 'ge' ``` **Steps to Reproduce** 1. Install vLLM from source using: ```bash git clone https://github.com/vllm-project/vllm.git cd vllm pip install . ``` 2. Run the vLLM API Server comma...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: py. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ction.__init__() got an unexpected keyword argument 'ge' ``` **Steps to Reproduce** 1. Install vLLM from source using: ```bash git clone https://github.com/vllm-project/vllm.git cd vllm pip install . ``` 2. Run the vLLM...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: rsing. ```bash poetry run python -m vllm.entrypoints.api_server \ --model SomeOrg/SomeModel \ --host 0.0.0.0 \ --port 8000 ``` **Error Message** ```bash Traceback (most recent call last): File "/path/to/python3.11/runpy...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: vLLM 0.7.3 TypeError in vllm.entrypoints.api_server Argument Parsing bug;stale ### Your current environment ### 🐛 Describe the bug When running vllm.entrypoints.api_server, I encounter a TypeError related to argparse ar...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
