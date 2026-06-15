# vllm-project/vllm#9573: [Bug]: The driver_worker gets stuck 100% of the time, when using Medusa with TP > 1

| 字段 | 值 |
| --- | --- |
| Issue | [#9573](https://github.com/vllm-project/vllm/issues/9573) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The driver_worker gets stuck 100% of the time, when using Medusa with TP > 1

### Issue 正文摘录

### Your current environment ### Model Input Dumps None ### 🐛 Describe the bug Run using the following command ```bash export CUDA_VISIBLE_DEVICES=0,1 export VLLM_ATTENTION_BACKEND="FLASH_ATTN" python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 30000 \ --served-model-name base_model --tokenizer-mode auto --max-model-len 2048 \ --max-num-batched-tokens 20480 --max-num-seqs 8 \ --tensor-parallel-size 2 --trust-remote-code \ --gpu-memory-utilization 0.8 --disable-custom-all-reduce --dtype float16 \ --speculative-model /home/work/qwen2/medusa \ --model /home/work/qwen2 \ --use-v2-block-manager --num-speculative-tokens 2 \ --enable-prefix-caching ``` The driver_worker is **stuck** here because the second worker (GPU) did not compute the logits returned by lm_head.linear_method.apply(). The phenomenon is that the second worker process reports an error "**No available block found in 60 seconds**". ```python #vllm/model_executor/layers/logits_processor.py def _get_logits( self, hidden_states: torch.Tensor, lm_head: VocabParallelEmbedding, embedding_bias: Optional[torch.Tensor], ) -> Optional[torch.Tensor]: logits = lm_head.linear_method.apply(lm_head, hidden_states, bias=...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: -model /home/work/qwen2/medusa \ --model /home/work/qwen2 \ --use-v2-block-manager --num-speculative-tokens 2 \ --enable-prefix-caching ``` The driver_worker is **stuck** here because the second worker (GPU) did not com...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: er_worker gets stuck 100% of the time, when using Medusa with TP > 1 bug;stale ### Your current environment ### Model Input Dumps None ### 🐛 Describe the bug Run using the following command ```bash export CUDA_VISIBLE_D...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: mote-code \ --gpu-memory-utilization 0.8 --disable-custom-all-reduce --dtype float16 \ --speculative-model /home/work/qwen2/medusa \ --model /home/work/qwen2 \ --use-v2-block-manager --num-speculative-tokens 2 \ --enabl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### 🐛 Describe the bug Run using the following command ```bash export CUDA_VISIBLE_DEVICES=0,1 export VLLM_ATTENTION_BACKEND="FLASH_ATTN" python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 30000 \ --ser...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: using Medusa with TP > 1 bug;stale ### Your current environment ### Model Input Dumps None ### 🐛 Describe the bug Run using the following command ```bash export CUDA_VISIBLE_DEVICES=0,1 export VLLM_ATTENTION_BACKEND="FL...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
