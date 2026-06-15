# vllm-project/vllm#39774: [Bug]: Inference qwen3.5 with tensor-parallel-size>1, RuntimeError: NCCL error: unhandled system error

| 字段 | 值 |
| --- | --- |
| Issue | [#39774](https://github.com/vllm-project/vllm/issues/39774) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Inference qwen3.5 with tensor-parallel-size>1, RuntimeError: NCCL error: unhandled system error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I use vllm 0.19 to inference qwen3.5 on 4*V100, the command as follows: CUDA_VISIBLE_DEVICES=0,1,2,3 vllm serve Qwen3.5-27B --max-model-len 20000 --gpu-memory-utilization 0.95 --host 0.0.0.0 --port 8010 --dtype half --reasoning-parser qwen3 --tensor-parallel-size 4 --enable-auto-tool-choice --tool-call-parser qwen3_coder I also tried qwen3-32B with --tensor-parallel-size 4, same error. qwen3-8B with -tensor-parallel-size 1, worked. changed with vllm 0.16 to inference qwen3.5, same error. The output as follows: (APIServer pid=1540417) INFO 04-14 13:46:36 [utils.py:299] (APIServer pid=1540417) INFO 04-14 13:46:36 [utils.py:299] █ █ █▄ ▄█ (APIServer pid=1540417) INFO 04-14 13:46:36 [utils.py:299] ▄▄ ▄█ █ █ █ ?▄? █ version 0.19.0 (APIServer pid=1540417) INFO 04-14 13:46:36 [utils.py:299] █▄█? █ █ █ █ model Qwen3.5-27B (APIServer pid=1540417) INFO 04-14 13:46:36 [utils.py:299] ?? ????? ????? ? ? (APIServer pid=1540417) INFO 04-14 13:46:36 [utils.py:299] (APIServer pid=1540417) INFO 04-14 13:46:36 [utils.py:233] non-default args: {'model_tag': 'Qwen3.5-27B', 'enable_auto_tool_choice': True, 'tool_call_parser': 'qwen3_coder', 'host': '0...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: =1540417) INFO 04-14 13:46:36 [utils.py:299] ▄▄ ▄█ █ █ █ ?▄? █ version 0.19.0 (APIServer pid=1540417) INFO 04-14 13:46:36 [utils.py:299] █▄█? █ █ █ █ model Qwen3.5-27B (APIServer pid=1540417) INFO 04-14 13:46:36 [utils....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: del-len 20000 --gpu-memory-utilization 0.95 --host 0.0.0.0 --port 8010 --dtype half --reasoning-parser qwen3 --tensor-parallel-size 4 --enable-auto-tool-choice --tool-call-parser qwen3_coder I also tried qwen3-32B with...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: I use vllm 0.19 to inference qwen3.5 on 4*V100, the command as follows: CUDA_VISIBLE_DEVICES=0,1,2,3 vllm serve Qwen3.5-27B --max-model-len 20000 --gpu-memory-utilization 0.95 --host 0.0.0.0 --port 8010 --dtype half --r...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: erver pid=1540417) INFO 04-14 13:46:36 [config.py:281] Setting attention block size to 784 tokens to ensure that attention page size is >= mamba page size. (APIServer pid=1540417) INFO 04-14 13:46:36 [config.py:312] Pad...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Inference qwen3.5 with tensor-parallel-size>1, RuntimeError: NCCL error: unhandled system error bug ### Your current environment ### 🐛 Describe the bug I use vllm 0.19 to inference qwen3.5 on 4*V100, the command...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
