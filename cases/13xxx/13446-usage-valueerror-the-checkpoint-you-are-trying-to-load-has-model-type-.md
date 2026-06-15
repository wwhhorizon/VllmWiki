# vllm-project/vllm#13446: [Usage]: ValueError: The checkpoint you are trying to load has model type `qwen2_5_vl` but Transformers does not recognize this architecture

| 字段 | 值 |
| --- | --- |
| Issue | [#13446](https://github.com/vllm-project/vllm/issues/13446) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: ValueError: The checkpoint you are trying to load has model type `qwen2_5_vl` but Transformers does not recognize this architecture

### Issue 正文摘录

### Your current environment ``` raise e File "/usr/local/lib/python3.12/dist-packages/vllm/transformers_utils/config.py", line 225, in get_config config = AutoConfig.from_pretrained( ^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/transformers/models/auto/configuration_auto.py", line 1073, in from_pretrained raise ValueError( ValueError: The checkpoint you are trying to load has model type `qwen2_5_vl` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date. You can update Transformers with the command `pip install --upgrade transformers`. If this does not work, and the checkpoint is very new, then there may not be a release version that supports this model yet. In this case, you can get the most up-to-date code by installing Transformers from source with the command `pip install git+https://github.com/huggingface/transformers.git` ``` ### How would you like to use vllm ``` docker run -it --name Qwen2.5-VL-7B-Instruct \ --gpus all \ -e TZ=Asia/Shanghai \ -v /data/modelsfiles/:/root/model \ -p 8444:8000 \ --ipc=host \ vllm/vllm-openai:v0.7.2 \ --mo...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: ValueError: The checkpoint you are trying to load has model type `qwen2_5_vl` but Transformers does not recognize this architecture usage;stale ### Your current environment ``` raise e File "/usr/local/lib/pyth...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: . This could be because of an issue with the checkpoint, or because your version of Transformers is out of date. You can update Transformers with the command `pip install --upgrade transformers`. If this does not work,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: oad has model type `qwen2_5_vl` but Transformers does not recognize this architecture usage;stale ### Your current environment ``` raise e File "/usr/local/lib/python3.12/dist-packages/vllm/transformers_utils/config.py"...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: `qwen2_5_vl` but Transformers does not recognize this architecture usage;stale ### Your current environment ``` raise e File "/usr/local/lib/python3.12/dist-packages/vllm/transformers_utils/config.py", line 225, in get_...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
