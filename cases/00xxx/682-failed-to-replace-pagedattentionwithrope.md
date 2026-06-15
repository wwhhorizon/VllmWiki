# vllm-project/vllm#682: Failed to replace PagedAttentionWithRoPE.

| 字段 | 值 |
| --- | --- |
| Issue | [#682](https://github.com/vllm-project/vllm/issues/682) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Failed to replace PagedAttentionWithRoPE.

### Issue 正文摘录

In my test.py, I intend to test and enhance the model's performance with longer input sequences. To achieve this, I need to modify the ModelConfig and PagedAttentionWithRoPE. However, I've encountered difficulties only when trying to modify the PagedAttentionWithRoPE component. More specifically: from vllm import LLM, SamplingParams from vllm.model_executor.layers.attention import PagedAttentionWithRoPE, PagedAttention from vllm.config import ModelConfig, _get_and_verify_dtype import torch from typing import List, Optional from vllm.transformers_utils.config import get_config import pdb ratio = 4 def __Configinit__( self, model: str, tokenizer: str, tokenizer_mode: str, trust_remote_code: bool, download_dir: Optional[str], use_np_weights: bool, use_dummy_weights: bool, dtype: str, seed: int, ) -> None: pdb.set_trace() self.model = model self.tokenizer = tokenizer self.tokenizer_mode = tokenizer_mode self.trust_remote_code = trust_remote_code self.download_dir = download_dir self.use_np_weights = use_np_weights self.use_dummy_weights = use_dummy_weights self.seed = seed self.hf_config = get_config(model, trust_remote_code) self.dtype = _get_and_verify_dtype(self.hf_config, dtype) s...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: PagedAttentionWithRoPE. In my test.py, I intend to test and enhance the model's performance with longer input sequences. To achieve this, I need to modify the ModelConfig and PagedAttentionWithRoPE. However, I've encoun...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: only when trying to modify the PagedAttentionWithRoPE component. More specifically: from vllm import LLM, SamplingParams from vllm.model_executor.layers.attention import PagedAttentionWithRoPE, PagedAttention from vllm....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: PagedAttention from vllm.config import ModelConfig, _get_and_verify_dtype import torch from typing import List, Optional from vllm.transformers_utils.config import get_config import pdb ratio = 4 def __Configinit__( sel...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: m] self.register_buffer("cos_sin_cache", cache, persistent=False) PagedAttentionWithRoPE.__init__ = __Ropeinit__ llm = LLM(model="OpenBuddy/openbuddy-openllama-7b-v5-fp16",tensor_parallel_size=4, max_num_batched_tokens=...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Failed to replace PagedAttentionWithRoPE. In my test.py, I intend to test and enhance the model's performance with longer input sequences. To achieve this, I need to modify the ModelConfig and PagedAttentionWithRoPE. Ho...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
