# vllm-project/vllm#19900: [Doc]: The documentation should be updated to cover GPU compatibility

| 字段 | 值 |
| --- | --- |
| Issue | [#19900](https://github.com/vllm-project/vllm/issues/19900) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support |
| 子分类 | env_compat |
| Operator 关键词 | triton |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Doc]: The documentation should be updated to cover GPU compatibility

### Issue 正文摘录

### 📚 The doc issue Today, I deployed the Qwen3 embedding model (version 0.9.1) on a V100 GPU. The model starts up without errors, but when making requests, I encounter the following error:​ ` asyncio.exceptions.CancelledError INFO: 10.1.1.38:60813 - "POST /v1/embeddings HTTP/1.1" 500 Internal Server Error (research) dev2@v100-02:~/zh$ /home/dev2/anaconda3/envs/research/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 7 leaked semaphore objects to clean up at shutdown warnings.warn('resource_tracker: There appear to be %d ' /home/dev2/anaconda3/envs/research/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 1 leaked shared_memory objects to clean up at shutdown warnings.warn('resource_tracker: There appear to be %d ' ` I noticed that the latest Triton version requires NVIDIA GPUs with Compute Capability 8.0 or higher. ![Image](https://github.com/user-attachments/assets/ca2a950c-796b-4584-b069-a42c538df5f2) ### Suggest a potential alternative/fix The documentation download page should include vLLM's hardware requirements. ### Before submitting a new issue... - [x] Make s...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: tation ### 📚 The doc issue Today, I deployed the Qwen3 embedding model (version 0.9.1) on a V100 GPU. The model starts up without errors, but when making requests, I encounter the following error:​ ` asyncio.exceptions....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: :60813 - "POST /v1/embeddings HTTP/1.1" 500 Internal Server Error (research) dev2@v100-02:~/zh$ /home/dev2/anaconda3/envs/research/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: T...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: U compatibility documentation ### 📚 The doc issue Today, I deployed the Qwen3 embedding model (version 0.9.1) on a V100 GPU. The model starts up without errors, but when making requests, I encounter the following error:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 'resource_tracker: There appear to be %d ' ` I noticed that the latest Triton version requires NVIDIA GPUs with Compute Capability 8.0 or higher. ![Image](https://github.com/user-attachments/assets/ca2a950c-796b-4584-b0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: .9.1) on a V100 GPU. The model starts up without errors, but when making requests, I encounter the following error:​ ` asyncio.exceptions.CancelledError INFO: 10.1.1.38:60813 - "POST /v1/embeddings HTTP/1.1" 500 Interna...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
