# vllm-project/vllm#9770: [Bug]: v6.3 Gibberish produced with long ctx (Machete + W4A16 + Spec Decoding)

| 字段 | 值 |
| --- | --- |
| Issue | [#9770](https://github.com/vllm-project/vllm/issues/9770) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v6.3 Gibberish produced with long ctx (Machete + W4A16 + Spec Decoding)

### Issue 正文摘录

Gibberish is not produced on the previous version with the same request. ### Your current environment --- ### 🐛 Describe the bug I start the inference server with: ```bash sudo docker run --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --env "HUGGING_FACE_HUB_TOKEN=xxx" \ -d \ -p 8003:8000 \ --ipc=host \ vllm/vllm-openai:latest \ --model neuralmagic/Meta-Llama-3.1-70B-Instruct-quantized.w4a16 \ --tensor-parallel-size 8 \ --gpu_memory_utilization 0.8 \ --speculative_model="ibm-fms/llama3-70b-accelerator" \ --speculative-draft-tensor-parallel-size 1 ``` Note the use of speculative decoding, tensor parallelism, and the draft parallel size. When running our pipeline, we occasionally get outputs that are clearly just random tokens strewn together. I can provide an example, but essentially, ~1 in 10 requests return gibberish regardless of content. (It gets worse the longer it is, I think). There are no error messages or warnings. I was wondering if anyone had encountered this issue or if someone at Neural Magic has any intuition for what could be causing it. Perhaps this has been addressed with the pending addition of parallel drafting? @alexm-neuralmagic @robertgshaw2-n...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: A16 + Spec Decoding) bug;stale Gibberish is not produced on the previous version with the same request. ### Your current environment --- ### 🐛 Describe the bug I start the inference server with: ```bash sudo docker run...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: 3 Gibberish produced with long ctx (Machete + W4A16 + Spec Decoding) bug;stale Gibberish is not produced on the previous version with the same request. ### Your current environment --- ### 🐛 Describe the bug I start the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: rallel-size 1 ``` Note the use of speculative decoding, tensor parallelism, and the draft parallel size. When running our pipeline, we occasionally get outputs that are clearly just random tokens strewn together. I can...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ce server with: ```bash sudo docker run --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --env "HUGGING_FACE_HUB_TOKEN=xxx" \ -d \ -p 8003:8000 \ --ipc=host \ vllm/vllm-openai:latest \ --model neuralmagic...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency Gibberish is not produced on the previous version with the same request.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
