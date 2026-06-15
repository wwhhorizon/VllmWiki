# vllm-project/vllm#39993: [Usage]: does vllm support Qwen3_5ForCausalLM architecture inference? not just Qwen3_5ForConditionalGeneration?

| 字段 | 值 |
| --- | --- |
| Issue | [#39993](https://github.com/vllm-project/vllm/issues/39993) |
| 状态 | open |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: does vllm support Qwen3_5ForCausalLM architecture inference? not just Qwen3_5ForConditionalGeneration?

### Issue 正文摘录

### Your current environment - vllm 0.19.0 - transformers 5.2.0 **I finetuned a language model based on Qwen3.5-9B, using the Qwen3_5ForCausalLM architecture.** `vllm serve Qwen3.5-9B-Stage2-2604 --port 8100 --tensor-parallel-size 1 --max-model-len 1024 --gpu-memory-utilization 0.6` ```text (APIServer pid=4191148) INFO 04-16 17:17:55 [utils.py:299] (APIServer pid=4191148) INFO 04-16 17:17:55 [utils.py:299] █ █ █▄ ▄█ (APIServer pid=4191148) INFO 04-16 17:17:55 [utils.py:299] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.19.0 (APIServer pid=4191148) INFO 04-16 17:17:55 [utils.py:299] █▄█▀ █ █ █ █ model /data/zhangqingguo/wangzejun/Text-Proofreading/two_stage/Qwen3.5-9B-Correction-Stage2-2604/ (APIServer pid=4191148) INFO 04-16 17:17:55 [utils.py:299] ▀▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀ ▀ (APIServer pid=4191148) INFO 04-16 17:17:55 [utils.py:299] (APIServer pid=4191148) INFO 04-16 17:17:55 [utils.py:233] non-default args: {'model_tag': '/data/zhangqingguo/wangzejun/Text-Proofreading/two_stage/Qwen3.5-9B-Correction-Stage2-2604/', 'port': 8100, 'model': '/data/zhangqingguo/wangzejun/Text-Proofreading/two_stage/Qwen3.5-9B-Correction-Stage2-2604/', 'max_model_len': 1024, 'gpu_memory_utilization': 0.5} (APIServer pid=4191148...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Usage]: does vllm support Qwen3_5ForCausalLM architecture inference? not just Qwen3_5ForConditionalGeneration? usage ### Your current environment - vllm 0.19.0 - transformers 5.2.0 **I finetuned a language model based...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: =4191148) INFO 04-16 17:17:55 [utils.py:299] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.19.0 (APIServer pid=4191148) INFO 04-16 17:17:55 [utils.py:299] █▄█▀ █ █ █ █ model /data/zhangqingguo/wangzejun/Text-Proofreading/two_stage/Qwen3....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: erver pid=4191148) INFO 04-16 17:17:57 [config.py:281] Setting attention block size to 272 tokens to ensure that attention page size is >= mamba page size. (APIServer pid=4191148) INFO 04-16 17:17:57 [config.py:312] Pad...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rypoints/cli/main.py", line 75, in main (APIServer pid=4191148) args.dispatch_function(args) (APIServer pid=4191148) File "/data/ENV/condaENVs/zhangqingguo/latest/lib/python3.11/site-packages/vllm/entrypoints/cli/serve....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Usage]: does vllm support Qwen3_5ForCausalLM architecture inference? not just Qwen3_5ForConditionalGeneration? usage ### Your current environment - vllm 0.19.0 - transformers 5.2.0 **I finetuned a language model based...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
