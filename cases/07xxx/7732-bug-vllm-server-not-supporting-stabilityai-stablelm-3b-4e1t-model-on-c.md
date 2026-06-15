# vllm-project/vllm#7732: [Bug]: vLLM server not supporting stabilityai/stablelm-3b-4e1t model on CPU 

| 字段 | 值 |
| --- | --- |
| Issue | [#7732](https://github.com/vllm-project/vllm/issues/7732) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM server not supporting stabilityai/stablelm-3b-4e1t model on CPU 

### Issue 正文摘录

### Your current environment - vLLM CPU v0.5.3.post1 - Model: stabilityai/stablelm-3b-4e1t - Dtype: FP16 or BF16 - AMD EPYC - 32 Core Processor - RAM: 100 GB ### 🐛 Describe the bug vLLM CPU v0.5.3.post1 container is getting killed while running inference on stabilityai/stablelm-3b-4e1t model with dtype FP16 and BF16 running on CPU. To reproduce the issue, run vLLM CPU container: ``` docker run -d --name vllm -p 8000:8000 -e HUGGING_FACE_HUB_TOKEN= -e VLLM_CPU_KVCACHE_SPACE=40 -e VLLM_CPU_OMP_THREADS_BIND=0-29 -v /mnt/models:/root/.cache/huggingface:rw cpu/vllm:v0.5.3.post1 --model=stabilityai/stablelm-3b-4e1t --dtype=float16 --max-model-len=2048 ``` Send infererence request to vLLM: ``` curl http://localhost:8000/v1/completions \ -H "Content-Type: application/json" \ -d '{ "model": "stabilityai/stablelm-3b-4e1t", "prompt": "Write short story about timetravel", "max_tokens": 50, "temperature": 0 }' ``` **Note : vLLM is working as expected when the model is loaded with dtype FP32.**

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ronment - vLLM CPU v0.5.3.post1 - Model: stabilityai/stablelm-3b-4e1t - Dtype: FP16 or BF16 - AMD EPYC - 32 Core Processor - RAM: 100 GB ### 🐛 Describe the bug vLLM CPU v0.5.3.post1 container is getting killed while run...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: vLLM server not supporting stabilityai/stablelm-3b-4e1t model on CPU bug;stale ### Your current environment - vLLM CPU v0.5.3.post1 - Model: stabilityai/stablelm-3b-4e1t - Dtype: FP16 or BF16 - AMD EPYC - 32 Core...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: LLM server not supporting stabilityai/stablelm-3b-4e1t model on CPU bug;stale ### Your current environment - vLLM CPU v0.5.3.post1 - Model: stabilityai/stablelm-3b-4e1t - Dtype: FP16 or BF16 - AMD EPYC - 32 Core Process...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: yai/stablelm-3b-4e1t model with dtype FP16 and BF16 running on CPU. To reproduce the issue, run vLLM CPU container: ``` docker run -d --name vllm -p 8000:8000 -e HUGGING_FACE_HUB_TOKEN= -e VLLM_CPU_KVCACHE_SPACE=40 -e V...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 16 running on CPU. To reproduce the issue, run vLLM CPU container: ``` docker run -d --name vllm -p 8000:8000 -e HUGGING_FACE_HUB_TOKEN= -e VLLM_CPU_KVCACHE_SPACE=40 -e VLLM_CPU_OMP_THREADS_BIND=0-29 -v /mnt/models:/roo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
