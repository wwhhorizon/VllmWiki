# vllm-project/vllm#9551: [Usage]: Custom LLM Generate

| 字段 | 值 |
| --- | --- |
| Issue | [#9551](https://github.com/vllm-project/vllm/issues/9551) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Custom LLM Generate

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I'm implementating a custom algorithm that requires a custom generate method. In this method, I need to access and store some of the attention outputs without running a full foward pass whole model as displayed below. But I keep getting errors related to `attn_metadata`. I tried multiple options such as using some of the abstractions in `attn_metadata.py` and `model_runner.py` but with no success. This very easy to do in transformers and I have a working it but I'm struggling to port it to vLLM. ```python import torch from vllm import LLM, SamplingParams from transformers import AutoTokenizer from typing import List, Tuple, Dict, Any, Optional model = LLM(model=model_name, dtype="bfloat16", gpu_memory_utilization=gpu_memory_utilization) model_obj = model.llm_engine.model_executor.driver_worker.model_runner.model hidden_states = model_obj.model.get_input_embeddings(input_ids) attention_outputs = [] cache_position = None past_key_values = None position_ids = None n_layers = 2 for layer in model_obj.model.layers[:n_layers]: if cache_position is None: past_seen_tokens = pa...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: g import List, Tuple, Dict, Any, Optional model = LLM(model=model_name, dtype="bfloat16", gpu_memory_utilization=gpu_memory_utilization) model_obj = model.llm_engine.model_executor.driver_worker.model_runner.model hidde...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: attn_type) File [/usr/local/lib/python3.11/dist-packages/vllm/attention/backends/flash_attn.py:584](http://157.157.221.29:17975/lab/tree/workspace/usr/local/lib/python3.11/dist-packages/vllm/attention/backends/flash_att...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nd I have a working it but I'm struggling to port it to vLLM. ```python import torch from vllm import LLM, SamplingParams from transformers import AutoTokenizer from typing import List, Tuple, Dict, Any, Optional model...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ole model as displayed below. But I keep getting errors related to `attn_metadata`. I tried multiple options such as using some of the abstractions in `attn_metadata.py` and `model_runner.py` but with no success. This v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: e some of the attention outputs without running a full foward pass whole model as displayed below. But I keep getting errors related to `attn_metadata`. I tried multiple options such as using some of the abstractions in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
