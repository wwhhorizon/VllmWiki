# vllm-project/vllm#39231: [Bug]: Qwen3.5 Text Only Model (Qwen3_5ForCausalLM)

| 字段 | 值 |
| --- | --- |
| Issue | [#39231](https://github.com/vllm-project/vllm/issues/39231) |
| 状态 | open |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5 Text Only Model (Qwen3_5ForCausalLM)

### Issue 正文摘录

**My current Environment:** ``` vLLM: 0.19.0 transformers: 5.5.0 ``` **Reproduction** ``` python3 -m vllm.entrypoints.openai.api_server \ --model principled-intelligence/Qwen3.5-0.8B-text-only \ --port 9100 \ --dtype bfloat16 \ --language-model-only ``` log: ``` (APIServer pid=783412) INFO 04-07 21:22:57 [utils.py:299] (APIServer pid=783412) INFO 04-07 21:22:57 [utils.py:299] █ █ █▄ ▄█ (APIServer pid=783412) INFO 04-07 21:22:57 [utils.py:299] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.19.0 (APIServer pid=783412) INFO 04-07 21:22:57 [utils.py:299] █▄█▀ █ █ █ █ model principled-intelligence/Qwen3.5-0.8B-text-only (APIServer pid=783412) INFO 04-07 21:22:57 [utils.py:299] ▀▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀ ▀ (APIServer pid=783412) INFO 04-07 21:22:57 [utils.py:299] (APIServer pid=783412) INFO 04-07 21:22:57 [utils.py:233] non-default args: {'port': 9100, 'model': 'principled-intelligence/Qwen3.5-0.8B-text-only', 'trust_remote_code': True, 'dtype': 'bfloat16', 'max_model_len': 4096, 'served_model_name': ['Qwen3.5-35B-A3B'], 'gpu_memory_utilization': 0.8, 'enable_prefix_caching': True, 'language_model_only': True} (APIServer pid=783412) INFO 04-07 21:23:26 [model.py:549] Resolved architecture: Qwen3_5ForCausalLM (APISe...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Qwen3.5 Text Only Model (Qwen3_5ForCausalLM) bug **My current Environment:** ``` vLLM: 0.19.0 transformers: 5.5.0 ``` **Reproduction** ``` python3 -m vllm.entrypoints.openai.api_server \ --model principled-intell...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: on** ``` python3 -m vllm.entrypoints.openai.api_server \ --model principled-intelligence/Qwen3.5-0.8B-text-only \ --port 9100 \ --dtype bfloat16 \ --language-model-only ``` log: ``` (APIServer pid=783412) INFO 04-07 21:...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: principled-intelligence/Qwen3.5-0.8B-text-only \ --port 9100 \ --dtype bfloat16 \ --language-model-only ``` log: ``` (APIServer pid=783412) INFO 04-07 21:22:57 [utils.py:299] (APIServer pid=783412) INFO 04-07 21:22:57 [...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: Server pid=783412) INFO 04-07 21:23:26 [config.py:281] Setting attention block size to 288 tokens to ensure that attention page size is >= mamba page size. (APIServer pid=783412) INFO 04-07 21:23:26 [config.py:312] Padd...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: True} (APIServer pid=783412) INFO 04-07 21:23:26 [model.py:549] Resolved architecture: Qwen3_5ForCausalLM (APIServer pid=783412) INFO 04-07 21:23:26 [model.py:1678] Using max model len 4096 (APIServer pid=783412) WARNIN...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
