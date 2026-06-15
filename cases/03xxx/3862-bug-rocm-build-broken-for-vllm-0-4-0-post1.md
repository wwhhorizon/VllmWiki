# vllm-project/vllm#3862: [Bug]: ROCm build broken for vllm 0.4.0.post1

| 字段 | 值 |
| --- | --- |
| Issue | [#3862](https://github.com/vllm-project/vllm/issues/3862) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: ROCm build broken for vllm 0.4.0.post1

### Issue 正文摘录

### Your current environment docker 26.0.0 ### 🐛 Describe the bug I followed https://docs.vllm.ai/en/latest/getting_started/amd-installation.html#build-from-source-docker-rocm to build a docker image of vllm with ROCm support. Building with the default ROCm 6.0 base image worked. However, when I ran the image using `docker run --network=host --group-add=video --ipc=host --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --shm-size 8G --device /dev/kfd --device /dev/dri vllm-rocm:v0.4.0.post1 python -m vllm.entrypoints.openai.api_server --model meta-llama/Llama-2-7b-chat-hf`, I got the following error. Seems like a version issue with numpy. ``` Traceback (most recent call last): File "/opt/conda/envs/py_3.9/lib/python3.9/runpy.py", line 197, in _run_module_as_main return _run_code(code, main_globals, None, File "/opt/conda/envs/py_3.9/lib/python3.9/runpy.py", line 87, in _run_code exec(code, run_globals) File "/opt/conda/envs/py_3.9/lib/python3.9/site-packages/vllm-0.4.0.post1+rocm603-py3.9-linux-x86_64.egg/vllm/entrypoints/openai/api_server.py", line 22, in from vllm.entrypoints.openai.serving_chat import OpenAIServingChat File "/opt/conda/envs/py_3.9/lib/python3.9/site-packag...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: ROCm build broken for vllm 0.4.0.post1 bug;rocm ### Your current environment docker 26.0.0 ### 🐛 Describe the bug I followed https://docs.vllm.ai/en/latest/getting_started/amd-installation.html#build-from-source-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ri vllm-rocm:v0.4.0.post1 python -m vllm.entrypoints.openai.api_server --model meta-llama/Llama-2-7b-chat-hf`, I got the following error. Seems like a version issue with numpy. ``` Traceback (most recent call last): Fil...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: ROCm build broken for vllm 0.4.0.post1 bug;rocm ### Your current environment docker 26.0.0 ### 🐛 Describe the bug I followed https://docs.vllm.ai/en/latest/getting_started/amd-installation.html#build-from-source-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ker 26.0.0 ### 🐛 Describe the bug I followed https://docs.vllm.ai/en/latest/getting_started/amd-installation.html#build-from-source-docker-rocm to build a docker image of vllm with ROCm support. Building with the defaul...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: in from outlines.fsm.regex import create_fsm_index_tokenizer, make_deterministic_fsm File "/opt/conda/envs/py_3.9/lib/python3.9/site-packages/outlines/fsm/regex.py", line 5, in import numba File "/opt/conda/envs/py_3.9/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
