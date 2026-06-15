# vllm-project/vllm#1873:  I can not improve throughput with tensor-parallel on multi-gpus.

| 字段 | 值 |
| --- | --- |
| Issue | [#1873](https://github.com/vllm-project/vllm/issues/1873) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

>  I can not improve throughput with tensor-parallel on multi-gpus.

### Issue 正文摘录

Hi dear： I have tested the tensor parallelism of vllm on multiple gpus, but the effect is not as good as running on a single card, even if the batch size is relatively large (such as 16, 32, 64) will not be good, what is the reason ? My service startup command is: CUDA_VISIBLE_DEVICES=0,1,2,3 python3 -m vllm.entrypoints.openai.api_server --dtype bfloat16 --max-model-len 7000 --tokenizer-mode auto --max-num-batched-tokens 30000 --block-size 16 --swap-space 16 --served-model-name codellama-13b-hf --model /home/models/CodeLlama-13b-hf/ --host 0.0.0.0 --port 8000 --tensor-parallel-size=4 --max-num-seqs 1024 thanks！

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: _VISIBLE_DEVICES=0,1,2,3 python3 -m vllm.entrypoints.openai.api_server --dtype bfloat16 --max-model-len 7000 --tokenizer-mode auto --max-num-batched-tokens 30000 --block-size 16 --swap-space 16 --served-model-name codel...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 2,3 python3 -m vllm.entrypoints.openai.api_server --dtype bfloat16 --max-model-len 7000 --tokenizer-mode auto --max-num-batched-tokens 30000 --block-size 16 --swap-space 16 --served-model-name codellama-13b-hf --model /...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nsor-parallel on multi-gpus. Hi dear： I have tested the tensor parallelism of vllm on multiple gpus, but the effect is not as good as running on a single card, even if the batch size is relatively large (such as 16, 32,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: I can not improve throughput with tensor-parallel on multi-gpus. Hi dear： I have tested the tensor parallelism of vllm on multiple gpus, but the effect is not as good as running on a single card, even if the batch size...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ax-model-len 7000 --tokenizer-mode auto --max-num-batched-tokens 30000 --block-size 16 --swap-space 16 --served-model-name codellama-13b-hf --model /home/models/CodeLlama-13b-hf/ --host 0.0.0.0 --port 8000 --tensor-para...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
