# vllm-project/vllm#6898: [Misc]: Problem about running with openvino

| 字段 | 值 |
| --- | --- |
| Issue | [#6898](https://github.com/vllm-project/vllm/issues/6898) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Problem about running with openvino

### Issue 正文摘录

### Anything you want to discuss about vllm. I run the openvino install by ``` docker build -f Dockerfile.openvino -t vllm-openvino-env . docker run -it --rm vllm-openvino-env ``` and start the code by ``` python3 -m vllm.entrypoints.openai.api_server --model {model_path} ``` The bug is shown below. Any help for this problem? ``` Traceback (most recent call last): [1/1922] File "/usr/lib/python3.8/runpy.py", line 194, in _run_module_as_main return _run_code(code, main_globals, None, File "/usr/lib/python3.8/runpy.py", line 87, in _run_code exec(code, run_globals) File "/usr/local/lib/python3.8/dist-packages/vllm/entrypoints/openai/api_server.py", line 312, in asyncio.run(run_server(args)) File "/usr/lib/python3.8/asyncio/runners.py", line 44, in run return loop.run_until_complete(main) File "/usr/lib/python3.8/asyncio/base_events.py", line 616, in run_until_complete return future.result() File "/usr/local/lib/python3.8/dist-packages/vllm/entrypoints/openai/api_server.py", line 289, in run_server app = await init_app(args, llm_engine) File "/usr/local/lib/python3.8/dist-packages/vllm/entrypoints/openai/api_server.py", line 229, in init_app if llm_engine is not None else AsyncLLMEng...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: penvino ### Anything you want to discuss about vllm. I run the openvino install by ``` docker build -f Dockerfile.openvino -t vllm-openvino-env . docker run -it --rm vllm-openvino-env ``` and start the code by ``` pytho...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nd start the code by ``` python3 -m vllm.entrypoints.openai.api_server --model {model_path} ``` The bug is shown below. Any help for this problem? ``` Traceback (most recent call last):
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: .8/dist-packages/vllm/config.py", line 181, in __init__ self._verify_quantization() File "/usr/local/lib/python3.8/dist-packages/vllm/config.py", line 218, in _verify_quantization quantization_override = method.override...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: n _check_marlin_supported major, minor = current_platform.get_device_capability() File "/usr/local/lib/python3.8/dist-packages/vllm/platforms/interface.py", line 28, in get_device_capability raise NotImplementedError No...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: nai/api_server.py", line 229, in init_app if llm_engine is not None else AsyncLLMEngine.from_engine_args( File "/usr/local/lib/python3.8/dist-packages/vllm/engine/async_llm_engine.py", line 455, in from_engine_args engi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
