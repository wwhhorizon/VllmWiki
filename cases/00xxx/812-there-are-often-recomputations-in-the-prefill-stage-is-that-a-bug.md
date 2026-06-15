# vllm-project/vllm#812: There are often recomputations in the prefill stage, is that a bug?

| 字段 | 值 |
| --- | --- |
| Issue | [#812](https://github.com/vllm-project/vllm/issues/812) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> There are often recomputations in the prefill stage, is that a bug?

### Issue 正文摘录

Here is my code in this file: vllm/worker/worker.py ```python @torch.inference_mode() def execute_model( self, seq_group_metadata_list: List[SequenceGroupMetadata], blocks_to_swap_in: Dict[int, int], blocks_to_swap_out: Dict[int, int], blocks_to_copy: Dict[int, List[int]], ) -> Dict[int, SequenceOutputs]: print(f"begin to run {len(seq_group_metadata_list)} groups") num = len(seq_group_metadata_list) need_prefill = False need_decoding = False if num > 1: for seq in seq_group_metadata_list: for k, v in seq.seq_data.items(): if len(v.output_token_ids) == 0: need_prefill = True else: need_decoding = True if need_prefill == True and need_decoding == True: import pdb; pdb.set_trace() ``` I want to capture such situation: a batched input with both sequence that need to run prefill and sequence that need to run decoding. Then I get this: ![image](https://github.com/vllm-project/vllm/assets/26128514/a68ce773-4327-46cc-b98e-383cd439602b) This group contains two sequence, the first one has generated 37 tokens, and the second one has no generated tokens, am I right? after this line of code: ```python # Prepare input tensors. input_tokens, input_positions, input_metadata = self._prepare_inputs...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: .inference_mode() def execute_model( self, seq_group_metadata_list: List[SequenceGroupMetadata], blocks_to_swap_in: Dict[int, int], blocks_to_swap_out: Dict[int, int], blocks_to_copy: Dict[int, List[int]], ) -> Dict[int...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e if need_prefill == True and need_decoding == True: import pdb; pdb.set_trace() ``` I want to capture such situation: a batched input with both sequence that need to run prefill and sequence that need to run decoding....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 39], num_generation_tokens=0, context_lens=tensor([], device='cuda:0', dtype=torch.int32), max_context_len=0), max_num_blocks_per_seq=0, block_tables=tensor([], device='cuda:0', dtype=torch.int32)), slot_mapping=tensor(...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s=[661, 739], num_generation_tokens=0, context_lens=tensor([], device='cuda:0', dtype=torch.int32), max_context_len=0), max_num_blocks_per_seq=0, block_tables=tensor([], device='cuda:0', dtype=torch.int32)), slot_mappin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: m/worker/worker.py ```python @torch.inference_mode() def execute_model( self, seq_group_metadata_list: List[SequenceGroupMetadata], blocks_to_swap_in: Dict[int, int], blocks_to_swap_out: Dict[int, int], blocks_to_copy:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
