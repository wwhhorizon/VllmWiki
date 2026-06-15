# vllm-project/vllm#8904: [Bug]: Tokenization Mismatch Between HuggingFace and vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#8904](https://github.com/vllm-project/vllm/issues/8904) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Tokenization Mismatch Between HuggingFace and vLLM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Tokenization mismatch between HuggingFace's AutoTokenizer and vLLM's tokenization for the `meta-llama/Llama-3.1-8B-Instruct` model (same issue using Mistral). This issue currently leads to incorrect token-level operations or unexpected behaviour in applications relying on precise tokenization. ### Code to Reproduce > The following example sets up the vllm inference server as well in order to closely reproduce our issue. ```python import subprocess import socket import requests import warnings from transformers import AutoTokenizer from urllib3.exceptions import InsecureRequestWarning import time def is_port_in_use(port): with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: return s.connect_ex(('localhost', port)) == 0 def start_server(model, port): cmd = f"python -m vllm.entrypoints.openai.api_server --model {model} --tensor-parallel-size 1 --port {port} --disable-frontend-multiprocessing --dtype bfloat16 --download-dir /mnt/models/ --gpu-memory-utilization 0.9 --enable-prefix-caching --max-model-len 8000" process = subprocess.Popen(cmd, shell=True) while not is_port_in_use(port): if process.poll() is not None: raise Runt...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: n-level operations or unexpected behaviour in applications relying on precise tokenization. ### Code to Reproduce > The following example sets up the vllm inference server as well in order to closely reproduce our issue...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Tokenization Mismatch Between HuggingFace and vLLM bug;stale ### Your current environment ### 🐛 Describe the bug Tokenization mismatch between HuggingFace's AutoTokenizer and vLLM's tokenization for the `meta-lla...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Tokenization Mismatch Between HuggingFace and vLLM bug;stale ### Your current environment ### 🐛 Describe the bug Tokenization mismatch between HuggingFace's AutoTokenizer and vLLM's tokenization for the `meta-lla...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ensor-parallel-size 1 --port {port} --disable-frontend-multiprocessing --dtype bfloat16 --download-dir /mnt/models/ --gpu-memory-utilization 0.9 --enable-prefix-caching --max-model-len 8000" process = subprocess.Popen(c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Tokenization Mismatch Between HuggingFace and vLLM bug;stale ### Your current environment ### 🐛 Describe the bug Tokenization mismatch between HuggingFace's AutoTokenizer and vLLM's tokenization for the `meta-lla...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
