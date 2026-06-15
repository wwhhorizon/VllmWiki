# vllm-project/vllm#28104: [Usage]: vllm bench serve不能用sharegpt数据集

| 字段 | 值 |
| --- | --- |
| Issue | [#28104](https://github.com/vllm-project/vllm/issues/28104) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: vllm bench serve不能用sharegpt数据集

### Issue 正文摘录

### Your current environment ```text 我运行以下bencmmarks命令：vllm bench serve --model Qwen3 --tokenizer /mnt/workspace/models --host 127.0.0.1 --port 80 --num-prompts 400 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 90,95,99 --dataset-name sharegpt --data set-path /mnt/workspace/benchmarks/sharegpt/ShareGPT_V3_unfiltered_cleaned_split.json --sharegpt-output-len 512 会报一下错误：/usr/local/lib/python3.12/dist-packages/torch/cuda/init.py:61: FutureWarning: The pynvml package is deprecated. Please install nvidia-ml-py instead. If you did not install pynvml directly, please report this to the maintainers of the package that installed pynvml for you. import pynvml # type: ignore[import] INFO 11-04 22:14:30 [init.py:243] Automatically detected platform cuda. INFO 11-04 22:14:32 [init.py:31] Available plugins for group vllm.general_plugins: INFO 11-04 22:14:32 [init.py:33] - lora_filesystem_resolver -> vllm.plugins.lora_resolvers.filesystem_resolver:register_filesystem_resolver INFO 11-04 22:14:32 [init.py:36] All plugins in this group will be loaded. Set to control which plugins to load. usage: vllm bench serve [options] vllm bench [options] serve: error: argument --dataset-name: in...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: cuda/init.py:61: FutureWarning: The pynvml package is deprecated. Please install nvidia-ml-py instead. If you did not install pynvml directly, please report this to the maintainers of the package that installed pynvml f...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: s --host 127.0.0.1 --port 80 --num-prompts 400 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 90,95,99 --dataset-name sharegpt --data set-path /mnt/workspace/benchmarks/sharegpt/ShareGPT_V3_unfiltered_clea...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: egpt-output-len 512 会报一下错误：/usr/local/lib/python3.12/dist-packages/torch/cuda/init.py:61: FutureWarning: The pynvml package is deprecated. Please install nvidia-ml-py instead. If you did not install pynvml directly, ple...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: # Your current environment ```text 我运行以下bencmmarks命令：vllm bench serve --model Qwen3 --tokenizer /mnt/workspace/models --host 127.0.0.1 --port 80 --num-prompts 400 --percentile-metrics ttft,tpot,itl,e2el --metric-percent...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: vllm bench serve不能用sharegpt数据集 usage;stale ### Your current environment ```text 我运行以下bencmmarks命令：vllm bench serve --model Qwen3 --tokenizer /mnt/workspace/models --host 127.0.0.1 --port 80 --num-prompts 400 --...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
