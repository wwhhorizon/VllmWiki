# vllm-project/vllm#34502: [Usage]: qwen3-vl-reranker-2b deploy issue

| 字段 | 值 |
| --- | --- |
| Issue | [#34502](https://github.com/vllm-project/vllm/issues/34502) |
| 状态 | open |
| 标签 | usage |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: qwen3-vl-reranker-2b deploy issue

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` OS : Ubuntu 22.04.3 LTS (x86_64) PyTorch version : 2.9.1+cu128 CUDA used to build PyTorch : 12.8 Python version : 3.10.12 (main, Jan 26 2026, 14:55:28) [GCC 11.4.0] (64-bit runtime) Is CUDA available : True CUDA runtime version : 12.0.140 GPU models and configuration : GPU 0: NVIDIA A10 Nvidia driver version : 470.129.06 [pip3] torch==2.9.1 [pip3] torchaudio==2.9.1 [pip3] torchvision==0.24.1 [pip3] transformers==4.57.6 [pip3] triton==3.5.1 vLLM Version : 0.15.1 ### How would you like to use vllm i wanna deploy qwen3-vl-reranker-2b model, and i tried 3 methods: 1. transformers 2. vllm local method: https://github.com/QwenLM/Qwen3-VL-Embedding/blob/main/examples/reranker_vllm.ipynb 3. vllm openai method: https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/vision_rerank_api_online.py take method 1 as standard answer, i found that method 2 have little difference, but the result of method 3 is exactly weird：all around 0.5X score. anyone can give me some advice? query and documents are all images. here is my code: ``` import requests import json def rerank(query_image_url, document_image_url...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ` ``` OS : Ubuntu 22.04.3 LTS (x86_64) PyTorch version : 2.9.1+cu128 CUDA used to build PyTorch : 12.8 Python version : 3.10.12 (main, Jan 26 2026, 14:55:28) [GCC 11.4.0] (64-bit runtime) Is CUDA available : True CUDA r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: qwen3-vl-reranker-2b deploy issue usage ### Your current environment ```text The output of `python collect_env.py` ``` OS : Ubuntu 22.04.3 LTS (x86_64) PyTorch version : 2.9.1+cu12
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: : Ubuntu 22.04.3 LTS (x86_64) PyTorch version : 2.9.1+cu128 CUDA used to build PyTorch : 12.8 Python version : 3.10.12 (main, Jan 26 2026, 14:55:28) [GCC 11.4.0] (64-bit runtime) Is CUDA available : True CUDA runtime ve...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: "model": "Qwen3-VL-Reranker-2B", # "instruction": "Retrieval relevant image or text with user's query", "query": query, "documents": documents, } # print(payload) response = requests.post( "http://localhost:8000/v2/rera...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dio==2.9.1 [pip3] torchvision==0.24.1 [pip3] transformers==4.57.6 [pip3] triton==3.5.1 vLLM Version : 0.15.1 ### How would you like to use vllm i wanna deploy qwen3-vl-reranker-2b model, and i tried 3 methods: 1. transf...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
