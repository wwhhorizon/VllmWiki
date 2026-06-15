# vllm-project/vllm#34534: [Bug]: EngineCore exits immediately after startup when vLLM CPU is launched from multiprocessing.Process on macOS

| 字段 | 值 |
| --- | --- |
| Issue | [#34534](https://github.com/vllm-project/vllm/issues/34534) |
| 状态 | open |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | cache;cuda;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: EngineCore exits immediately after startup when vLLM CPU is launched from multiprocessing.Process on macOS

### Issue 正文摘录

### Current environment - vLLM version: 0.15.1+cpu (built from source following [CPU full build docs](https://docs.vllm.ai/en/latest/getting_started/installation/cpu/#full-build)) - Python: 3.12.11 - OS: macOS (Darwin 24.6.0, Apple Silicon) - Hardware: CPU only (no GPU) ### Model TinyLlama/TinyLlama-1.1B-Chat-v1.0 ### How to reproduce Launch vLLM's `run_server` from within a `multiprocessing.Process` child process on macOS: ```python import multiprocessing import os import uvloop from vllm.entrypoints.openai.api_server import run_server from vllm.entrypoints.openai.cli_args import make_arg_parser, validate_parsed_serve_args from vllm.entrypoints.utils import cli_env_setup from vllm.utils.argparse_utils import FlexibleArgumentParser def vllm_kickoff(): cli_env_setup() parser = FlexibleArgumentParser(description="vLLM server") parser = make_arg_parser(parser) args = parser.parse_args([ "--model", "TinyLlama/TinyLlama-1.1B-Chat-v1.0", "--port", "8006", ]) validate_parsed_serve_args(args) uvloop.run(run_server(args)) proc = multiprocessing.Process(target=vllm_kickoff) proc.start() proc.join() ``` The parent process could be a FastAPI app running under uvicorn, as in the [llm-d launche...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: m multiprocessing.Process on macOS stale ### Current environment - vLLM version: 0.15.1+cpu (built from source following [CPU full build docs](https://docs.vllm.ai/en/latest/getting_started/installation/cpu/#full-build)...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: startup when vLLM CPU is launched from multiprocessing.Process on macOS stale ### Current environment - vLLM version: 0.15.1+cpu (built from source following [CPU full build docs](https://docs.vllm.ai/en/latest/getting_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: macOS (Darwin 24.6.0, Apple Silicon) - Hardware: CPU only (no GPU) ### Model TinyLlama/TinyLlama-1.1B-Chat-v1.0 ### How to reproduce Launch vLLM's `run_server` from within a `multiprocessing.Process` child process on ma...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: lt from source following [CPU full build docs](https://docs.vllm.ai/en/latest/getting_started/installation/cpu/#full-build)) - Python: 3.12.11 - OS: macOS (Darwin 24.6.0, Apple Silicon) - Hardware: CPU only (no GPU) ###...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ;frontend_api;hardware_porting;model_support;scheduler_memory cache;cuda;triton build_error dtype;env_dependency Current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
