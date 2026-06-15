# vllm-project/vllm#14760: [Bug]: Error when split pp

| 字段 | 值 |
| --- | --- |
| Issue | [#14760](https://github.com/vllm-project/vllm/issues/14760) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Error when split pp

### Issue 正文摘录

### Your current environment https://github.com/vllm-project/vllm/blame/f53a0586b9c88a78167157296555b7664c398055/vllm/config.py#L905 pp_rank = parallel_config.rank // parallel_config.tensor_parallel_size pp_size = parallel_config.pipeline_parallel_size start, end = get_pp_indices(total_num_hidden_layers, pp_rank, pp_size) it seem confuse, maybe `pp_rank=parallel_config.rank %parallel_config.pipeline_parallel_size` is expect? ### 🐛 Describe the bug def get_layers_start_end_indices( self, parallel_config: "ParallelConfig") -> tuple[int, int]: from vllm.distributed.utils import get_pp_indices if self.hf_text_config.model_type == "deepseek_mtp": total_num_hidden_layers = getattr(self.hf_text_config, "num_nextn_predict_layers", 0) else: total_num_hidden_layers = getattr(self.hf_text_config, "num_hidden_layers", 0) pp_rank = parallel_config.rank % parallel_config.pipeline_parallel_size pp_size = parallel_config.pipeline_parallel_size start, end = get_pp_indices(total_num_hidden_layers, pp_rank, pp_size) return start, end ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documenta...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: om/vllm-project/vllm/blame/f53a0586b9c88a78167157296555b7664c398055/vllm/config.py#L905 pp_rank = parallel_config.rank // parallel_config.tensor_parallel_size pp_size = parallel_config.pipeline_parallel_size start, end...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ParallelConfig") -> tuple[int, int]: from vllm.distributed.utils import get_pp_indices if self.hf_text_config.model_type == "deepseek_mtp": total_num_hidden_layers = getattr(self.hf_text_config, "num_nextn_predict_layer
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: end ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: "num_nextn_predict_layers", 0) else: total_num_hidden_layers = getattr(self.hf_text_config, "num_hidden_layers", 0) pp_rank = parallel_config.rank % parallel_config.pipeline_parallel_siz
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Error when split pp bug;stale ### Your current environment https://github.com/vllm-project/vllm/blame/f53a0586b9c88a78167157296555b7664c398055/vllm/config.py#L905 pp_rank = parallel_config.rank // parallel_config...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
