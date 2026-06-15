# vllm-project/vllm#30893: [Bug]: V1 Engine splits offline embedding batches unexpectedly when multiprocessing is enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#30893](https://github.com/vllm-project/vllm/issues/30893) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: V1 Engine splits offline embedding batches unexpectedly when multiprocessing is enabled

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary When using llm.embed() for offline inference with V1 Engine (vLLM 0.12.0), batches of 8 prompts submitted together are split into suboptimal batches (typically 1+7 or 2+6) instead of being processed as a single batch. This behavior only occurs when multiprocessing is enabled (default). **Expected behavior** 8 calls to llm.embed(batch_of_8) → 8 GPU forward passes **Actual behavior** 8 calls to llm.embed(batch_of_8) → ~16 GPU forward passes (batches split as 1+7, 2+6, 3+5, etc.) ## Minimal Reproducible Example ```python from vllm import LLM def main(): llm = LLM( model="BAAI/bge-large-en-v1.5", max_model_len=384, max_num_seqs=8, max_num_batched_tokens=3072, ) prompts = ["What is the capital of France?"] * 64 # 8 by 8 for i in range(0, len(prompts), 8): batch = prompts[i : i + 8] result = llm.embed(batch) if __name__ == "__main__": main() ``` ### Evidence from GPU Model Runner Logs **Expected** Batches of 72 tokens (8 × 9) **Actual** Batch | num_tokens | Requests | Expected -- | -- | -- | -- 1 | 9 | 1 | 72 (8) 2 | 63 | 7 | — 3 | 9 | 1 | 72 (8) 4 | 63 | 7 | — ... | ... | ... | The pattern shows the first request arrives at...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: forward passes (batches split as 1+7, 2+6, 3+5, etc.) ## Minimal Reproducible Example ```python from vllm import LLM def main(): llm = LLM( model="BAAI/bge-large-en-v1.5", max_model_len=384, max_num_seqs=8, max_num_batc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: nd is scheduled immediately, before the remaining requests have been transmitted through the ZMQ socket. ## Environment vLLM: 0.12.0 GPU: T4 (Google Colab) Model: BAAI/bge-large-en-v1.5 ## Questions - Is this considered...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ration to make the scheduler wait briefly for additional requests before dispatching (e.g., a batching timeout)? **Related**: This may be connected to #25842 (concurrency issues with encoder-based embedders in V1 Engine...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: `python from vllm import LLM def main(): llm = LLM( model="BAAI/bge-large-en-v1.5", max_model_len=384, max_num_seqs=8, max_num_batched_tokens=3072, ) prompts = ["What is the capital of France?"] * 64 # 8 by 8 for
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Expected** Batches of 72 tokens (8 × 9) **Actual** Batch | num_tokens | Requests | Expected -- | -- | -- | -- 1 | 9 | 1 | 72 (8) 2 | 63 | 7 | — 3 | 9 | 1 | 72 (8) 4 | 63 | 7 | — ... | ... | ... | The pattern shows the f...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
