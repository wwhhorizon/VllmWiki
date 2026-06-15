# vllm-project/vllm#35395: [Feature]:  Support for transformers 5.2.0

| 字段 | 值 |
| --- | --- |
| Issue | [#35395](https://github.com/vllm-project/vllm/issues/35395) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]:  Support for transformers 5.2.0

### Issue 正文摘录

https://huggingface.co/Qwen/Qwen3.5-27B-FP8 (APIServer pid=1190) INFO 02-26 21:10:02 [utils.py:287] (APIServer pid=1190) INFO 02-26 21:10:02 [utils.py:287] █ █ █▄ ▄█ (APIServer pid=1190) INFO 02-26 21:10:02 [utils.py:287] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.16.0 (APIServer pid=1190) INFO 02-26 21:10:02 [utils.py:287] █▄█▀ █ █ █ █ model Qwen/Qwen3.5-27B-FP8 (APIServer pid=1190) INFO 02-26 21:10:02 [utils.py:287] ▀▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀ ▀ (APIServer pid=1190) INFO 02-26 21:10:02 [utils.py:287] (APIServer pid=1190) INFO 02-26 21:10:02 [utils.py:223] non-default args: {'model_tag': 'Qwen/Qwen3.5-27B-FP8', 'api_server_count': 1, 'host': '0.0.0.0', 'port': 8003, 'model': 'Qwen/Qwen3.5-27B-FP8', 'trust_remote_code': True, 'max_model_len': 262144, 'reasoning_parser': 'qwen3', 'enable_prefix_caching': True} (APIServer pid=1190) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. (APIServer pid=1190) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. (APIServer pid=1190) Traceback (most recent call last): (APIServer pid=1190) File "/home/cheng/vllm/venv/bin/vllm", line 6, in (APIServer pid=1190) sys.ex...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: pid=1190) INFO 02-26 21:10:02 [utils.py:287] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.16.0 (APIServer pid=1190) INFO 02-26 21:10:02 [utils.py:287] █▄█▀ █ █ █ █ model Qwen/Qwen3.5-27B-FP8 (APIServer pid=1190) INFO 02-26 21:10:02 [uti...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: Support for transformers 5.2.0 feature request https://huggingface.co/Qwen/Qwen3.5-27B-FP8 (APIServer pid=1190) INFO 02-26 21:10:02 [utils.py:287] (APIServer pid=1190) INFO 02-26 21:10:02 [utils.py:287] █ █ █...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: entrypoints/cli/main.py", line 73, in main (APIServer pid=1190) args.dispatch_function(args) (APIServer pid=1190) File "/home/cheng/vllm/venv/lib/python3.12/site-packages/vllm/entrypoints/cli/serve.py", line 111, in cmd...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ansformers 5.2.0 feature request https://huggingface.co/Qwen/Qwen3.5-27B-FP8 (APIServer pid=1190) INFO 02-26 21:10:02 [utils.py:287] (APIServer pid=1190) INFO 02-26 21:10:02 [utils.py:287] █ █ █▄ ▄█ (APIServer pid=1190)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: o load has model type `qwen3_5` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date. (APIServer pid=1190)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
