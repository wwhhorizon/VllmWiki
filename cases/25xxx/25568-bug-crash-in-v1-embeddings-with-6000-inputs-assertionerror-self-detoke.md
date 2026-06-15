# vllm-project/vllm#25568: [Bug]: Crash in /v1/embeddings with ~6000 inputs (AssertionError: self.detokenizer is not None) Model: Qwen/Qwen3-Embedding-0.6B

| 字段 | 值 |
| --- | --- |
| Issue | [#25568](https://github.com/vllm-project/vllm/issues/25568) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Crash in /v1/embeddings with ~6000 inputs (AssertionError: self.detokenizer is not None) Model: Qwen/Qwen3-Embedding-0.6B

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug [collect env py result.txt](https://github.com/user-attachments/files/22510391/collect.env.py.result.txt) [VLLMERROR.txt](https://github.com/user-attachments/files/22510390/VLLMERROR.txt) ### ✅ Steps to Reproduce 1. Run the latest vLLM docker image (`vLLM 0.10.1.1`, see env details below). 2. Use the following minimal Python snippet to reproduce: ```python import requests, json, numpy as np EXTERNAL_VECTOR_SERVICE_ENDPOINT = "http://localhost:8000/v1/embeddings" EXTERNAL_VECTOR_SERVICE_MODEL = "Qwen/Qwen3-Embedding-0.6B" def get_embedding(texts: list): url = EXTERNAL_VECTOR_SERVICE_ENDPOINT headers = {'Content-Type': 'application/json'} payload = { "input": texts, # around 6000 items in the list "model": EXTERNAL_VECTOR_SERVICE_MODEL } response = requests.post(url, headers=headers, data=json.dumps(payload)) response.raise_for_status() data = response.json() return np.array([item["embedding"] for item in data["data"]], dtype=np.float64) texts = ["some text", "混合语言测试", "another sample", ...] * 6000 embeddings = get_embedding(texts) ``` 3. Observe that the server crashes. 4. Sending the same code with >10,000 items works fine. --- #...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: 2510390/VLLMERROR.txt) ### ✅ Steps to Reproduce 1. Run the latest vLLM docker image (`vLLM 0.10.1.1`, see env details below). 2. Use the following minimal Python snippet to reproduce: ```python import requests, json, nu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 1 (production docker image) * **Model**: `Qwen/Qwen3-Embedding-0.6B` * **CUDA**: 12.8.93, cuDNN 9.7.1.26 * **GPU**: NVIDIA GeForce RTX 4060 Laptop GPU (Driver 580.65.06) ### Before submitting a new issue... - [x] Make s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: eddings with ~6000 inputs (AssertionError: self.detokenizer is not None) Model: Qwen/Qwen3-Embedding-0.6B bug ### Your current environment ### 🐛 Describe the bug [collect env py result.txt](https://github.com/user-attac...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ithub.com/user-attachments/files/22510390/VLLMERROR.txt) ### ✅ Steps to Reproduce 1. Run the latest vLLM docker image (`vLLM 0.10.1.1`, see env details below). 2. Use the following minimal Python snippet to reproduce: `...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: json() return np.array([item["embedding"] for item in data["data"]], dtype=np.float64) texts = ["some text", "混合语言测试", "another sample", ...] * 6000 embeddings = get_embedding(texts) ``` 3. Observe that the server crash...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
