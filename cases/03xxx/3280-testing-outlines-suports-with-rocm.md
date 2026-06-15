# vllm-project/vllm#3280: testing outlines suports with ROCM

| 字段 | 值 |
| --- | --- |
| Issue | [#3280](https://github.com/vllm-project/vllm/issues/3280) |
| 状态 | closed |
| 标签 | bug;rocm;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support |
| 子分类 | cold_start |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> testing outlines suports with ROCM

### Issue 正文摘录

requirements-rocm.txt missing outlines: ``` outlines >= 0.0.27 ``` after adding outlines, running openai api server has error: ``` root@dualamd:/app# python -m vllm.entrypoints.openai.api_server \ > --gpu-memory-utilization 0.98 --trust-remote-code \ > --served-model-name gpt-3.5-turbo-1106 \ > --max-model-len 32768 --model Qwen1.5-14B Traceback (most recent call last): File "/opt/conda/envs/py_3.9/lib/python3.9/runpy.py", line 197, in _run_module_as_main return _run_code(code, main_globals, None, File "/opt/conda/envs/py_3.9/lib/python3.9/runpy.py", line 87, in _run_code exec(code, run_globals) File "/opt/conda/envs/py_3.9/lib/python3.9/site-packages/vllm-0.3.3+rocm603-py3.9-linux-x86_64.egg/vllm/entrypoints/openai/api_server.py", line 23, in from vllm.entrypoints.openai.serving_chat import OpenAIServingChat File "/opt/conda/envs/py_3.9/lib/python3.9/site-packages/vllm-0.3.3+rocm603-py3.9-linux-x86_64.egg/vllm/entrypoints/openai/serving_chat.py", line 15, in from vllm.model_executor.guided_decoding import get_guided_decoding_logits_processor File "/opt/conda/envs/py_3.9/lib/python3.9/site-packages/vllm-0.3.3+rocm603-py3.9-linux-x86_64.egg/vllm/model_executor/guided_decoding.py",...

## 现有链接修复摘要

#43814 [Bugfix][SM120] Enable CUTLASS grouped GEMM (MoE) for SM_120/SM_121 consumer Blackwell

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: _server.py", line 23, in from vllm.entrypoints.openai.serving_chat import OpenAIServingChat File "/opt/conda/envs/py_3.9/lib/python3.9/site-packages/vllm-0.3.3+rocm603-py3.9-linux-x86_64.egg/vllm/entrypoints/openai/serv...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: testing outlines suports with ROCM bug;rocm;stale requirements-rocm.txt missing outlines: ``` outlines >= 0.0.27 ``` after adding outlines, running openai api server has error: ``` root@dualamd:/app# python -m vllm.entr...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: _support cuda crash env_dependency #43814 [Bugfix][SM120] Enable CUTLASS grouped GEMM (MoE) for SM_120/SM_121 consumer Blackwell requirements-rocm.txt missing outlines:
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: r \ > --gpu-memory-utilization 0.98 --trust-remote-code \ > --served-model-name gpt-3.5-turbo-1106 \ > --max-model-len 32768 --model Qwen1.5-14B Traceback (most recent call last): File "/opt/conda/envs/py_3.9/lib/python...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: testing outlines suports with ROCM bug;rocm;stale requirements-rocm.txt missing outlines: ``` outlines >= 0.0.27 ``` after adding outlines, running openai api server has error: ``` root@dualamd:/app# python -m vllm.entry

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43814](https://github.com/vllm-project/vllm/pull/43814) | mentioned | 0.6 | [Bugfix][SM120] Enable CUTLASS grouped GEMM (MoE) for SM_120/SM_121 consumer Blackwell | on ran on physical DGX Spark hardware. Related CUTLASS upstream PR: [NVIDIA/cutlass#3280](https://github.com/NVIDIA/cutlass/pull/3280) |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
