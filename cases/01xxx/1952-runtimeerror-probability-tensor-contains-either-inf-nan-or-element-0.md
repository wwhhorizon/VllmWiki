# vllm-project/vllm#1952: RuntimeError: probability tensor contains either `inf`, `nan` or element < 0

| 字段 | 值 |
| --- | --- |
| Issue | [#1952](https://github.com/vllm-project/vllm/issues/1952) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> RuntimeError: probability tensor contains either `inf`, `nan` or element < 0

### Issue 正文摘录

when I use LLama2-70B(AWQ quantized) and the input more than 4096 tokens, I get the error 'RuntimeError: probability tensor contains either `inf`, `nan` or element ', 'eos_token': ' ', 'unk_token': ' '}, clean_up_tokenization_spaces=False), added_tokens_decoder={ 0: AddedToken(" ", rstrip=False, lstrip=False, single_word=False, normalized=True, special=True), 1: AddedToken(" ", rstrip=False, lstrip=False, single_word=False, normalized=True, special=True), 2: AddedToken(" ", rstrip=False, lstrip=False, single_word=False, normalized=True, special=True), } AsyncEngineArgs(model='/home/services/AWQ_model', tokenizer='/home/services/AWQ_model', tokenizer_mode='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', seed=0, max_model_len=10000, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=4, block_size=16, swap_space=4, gpu_memory_utilization=0.8, max_num_batched_tokens=10000, max_num_seqs=64, max_paddings=256, disable_log_stats=False, revision=None, tokenizer_revision=None, quantization='awq', engine_use_ray=False, disable_log_requests=False, max_log_len=None)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: robability tensor contains either `inf`, `nan` or element < 0 when I use LLama2-70B(AWQ quantized) and the input more than 4096 tokens, I get the error 'RuntimeError: probability tensor contains either `inf`, `nan` or e...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: or contains either `inf`, `nan` or element < 0 when I use LLama2-70B(AWQ quantized) and the input more than 4096 tokens, I get the error 'RuntimeError: probability tensor contains either `inf`, `nan` or element ', 'eos_...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ', 'eos_token': ' ', 'unk_token': ' '}, clean_up_tokenization_spaces=False), added_tokens_decoder={ 0: AddedToken(" ", rstrip=False, lstrip=False, single_word=False, normalized=True, special=True), 1: AddedToken(" ", rs...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ', 'unk_token': ' '}, clean_up_tokenization_spaces=False), added_tokens_decoder={ 0: AddedToken(" ", rstrip=False, lstrip=False, single_word=False, normalized=True, special=True), 1: AddedToken(" ", rstrip=False, lstrip...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: (" ", rstrip=False, lstrip=False, single_word=False, normalized=True, special=True), 1: AddedToken(" ", rstrip=False, lstrip=False, single_word=False, normalized=True, special=True), 2: AddedToken(" ", rstrip=False, lst...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
