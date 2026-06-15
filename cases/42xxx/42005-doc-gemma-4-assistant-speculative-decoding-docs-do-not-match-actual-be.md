# vllm-project/vllm#42005: [Doc]: Gemma 4 assistant speculative decoding docs do not match actual behavior on vLLM 0.20.1

| 字段 | 值 |
| --- | --- |
| Issue | [#42005](https://github.com/vllm-project/vllm/issues/42005) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Gemma 4 assistant speculative decoding docs do not match actual behavior on vLLM 0.20.1

### Issue 正文摘录

### 📚 The doc issue **Environment** vLLM version: 0.20.1 Launch method: vllm serve GPU: single GPU via CUDA_VISIBLE_DEVICES=0 Model under test: gemma-4-E2B-it Speculative config: assistant model via google/gemma-4-E2B-it-assistant Relevant docs currently show Gemma 4 assistant-model speculative decoding examples, and the Gemma 4 recipe presents this as a supported usage path. **Reproduction** I tried to run Gemma 4 assistant speculative decoding on vllm==0.20.1 with the following command: CUDA_VISIBLE_DEVICES=0 vllm serve google/gemma-4-E2B-it \ --host 0.0.0.0 \ --port 8002 \ --tensor-parallel-size 1 \ --max-model-len 8192 \ --speculative-config '{"model": "google/gemma-4-E2B-it-assistant", "num_speculative_tokens": 4}' The attached runtime log shows the full startup sequence and failure during engine initialization. **Expected** Based on the current Gemma 4 documentation, I expected the documented assistant-model speculative decoding path to start successfully, or at minimum for the documentation to clearly state that this path is not supported on the latest stable PyPI release. **Actual** Engine initialization fails with the following error: NotImplementedError: Speculative Deco...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Doc]: Gemma 4 assistant speculative decoding docs do not match actual behavior on vLLM 0.20.1 documentation ### 📚 The doc issue **Environment** vLLM version: 0.20.1 Launch method: vllm serve GPU: single GPU via CUDA_VI...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: r on vLLM 0.20.1 documentation ### 📚 The doc issue **Environment** vLLM version: 0.20.1 Launch method: vllm serve GPU: single GPU via CUDA_VISIBLE_DEVICES=0 Model under test: gemma-4-E2B-it Speculative config: assistant...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 4B \ --host 0.0.0.0 \ --port 8002 \ --tensor-parallel-size 1 \ --dtype bfloat16 \ --max-model-len 131072 \ --block-size 16 \ --gpu-memory-utilization 0.9 \ --max-num-seqs 2 \ --max-num-batched-tokens 4096 \ --enable-pre...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Doc]: Gemma 4 assistant speculative decoding docs do not match actual behavior on vLLM 0.20.1 documentation ### 📚 The doc issue **Environment** vLLM version: 0.20.1 Launch method: vllm serve GPU: single GPU via CUDA_VI...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ent** vLLM version: 0.20.1 Launch method: vllm serve GPU: single GPU via CUDA_VISIBLE_DEVICES=0 Model under test: gemma-4-E2B-it Speculative config: assistant model via google/gemma-4-E2B-it-assistant Relevant docs curr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
