# vllm-project/vllm#6648: [Usage]: How to fix the batch size whiling decoding？

| 字段 | 值 |
| --- | --- |
| Issue | [#6648](https://github.com/vllm-project/vllm/issues/6648) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to fix the batch size whiling decoding？

### Issue 正文摘录

### Your current environment ```text export VLLM_USE_FLASH_ATTN_TRITON=0 export PYTORCH_TUNABLEOP_ENABLED=1 export PYTORCH_TUNABLEOP_FILENAME=tuned.csv export PYTORCH_TUNABLEOP_TUNING=0 export HIP_VISIBLE_DEVICES=6,7 export TOKENIZERS_PARALLELISM=false torchrun --standalone --nproc_per_node=2 \ benchmark_throughput.py \ --model /data/models/Llama-2-70b-hf \ --num-prompts=32 \ --input-len 2048 \ --output-len 200 \ --tensor-parallel-size 2 \ --trust-remote-code \ --dtype bfloat16 ``` ### How would you like to use vllm **Question 1:** When running the above script on an AMD GPU, I set the number of prompts and the input/output lengths. --num-prompts=32 \ --input-len 2048 \ --output-len 200 \ I expected the batch size to be 8 during the decoding process, such as when executing the paged attention v2 kernel. However, when I added print statements in the file csrc/attention/attention_kernels.cu as blow: ``` void paged_attention_v2( torch::Tensor& out, // [num_seqs, num_heads, head_size] torch::Tensor& exp_sums, // [num_seqs, num_heads, max_num_partitions] torch::Tensor& max_logits, // [num_seqs, num_heads, max_num_partitions] torch::Tensor& tmp_out, // [num_seqs, num_heads, max_num_part...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: --output-len 200 \ --tensor-parallel-size 2 \ --trust-remote-code \ --dtype bfloat16 ``` ### How would you like to use vllm **Question 1:** When running the above script on an AMD GPU, I set the number of prompts and th...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: TUNING=0 export HIP_VISIBLE_DEVICES=6,7 export TOKENIZERS_PARALLELISM=false torchrun --standalone --nproc_per_node=2 \ benchmark_throughput.py \ --model /data/models/Llama-2-70b-hf \ --num-prompts=32 \ --input-len 2048...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: torchrun --standalone --nproc_per_node=2 \ benchmark_throughput.py \ --model /data/models/Llama-2-70b-hf \ --num-prompts=32 \ --input-len 2048 \ --output-len 200 \ --tensor-parallel-size 2 \ --trust-remote-code \ --dtyp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: e;stale ### Your current environment ```text export VLLM_USE_FLASH_ATTN_TRITON=0 export PYTORCH_TUNABLEOP_ENABLED=1 export PYTORCH_TUNABLEOP_FILENAME=tuned.csv export PYTORCH_TUNABLEOP_TUNING=0 export HIP_VISIBLE_DEVICE...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: _TUNABLEOP_FILENAME=tuned.csv export PYTORCH_TUNABLEOP_TUNING=0 export HIP_VISIBLE_DEVICES=6,7 export TOKENIZERS_PARALLELISM=false torchrun --standalone --nproc_per_node=2 \ benchmark_throughput.py \ --model /data/model...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
