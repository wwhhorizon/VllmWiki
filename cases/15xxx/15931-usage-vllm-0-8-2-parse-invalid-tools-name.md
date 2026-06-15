# vllm-project/vllm#15931: [Usage]: vllm 0.8.2 parse invalid tools name

| 字段 | 值 |
| --- | --- |
| Issue | [#15931](https://github.com/vllm-project/vllm/issues/15931) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | race_cond |
| Operator 关键词 | cuda |
| 症状 | mismatch |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: vllm 0.8.2 parse invalid tools name

### Issue 正文摘录

### Your current environment ```text vllm 0.8.2 docker System ubuntu 24.04 GPU 4090 48GB x 8 CPU 7950WX DRAM 1TB DDR5 CUDA 12.8 ``` ### How would you like to use vllm ```text vllm 0.8.2 sudo docker run --runtime nvidia --gpus all \ -d \ -v /root/models:/models \ -p 5536:8000 \ --env "HF_HUB_OFFLINE=1" \ --ipc=host \ vllm/vllm-openai:latest \ --model /models/Qwen/QwQ-32B \ --served_model_name QwQ-32B \ --gpu_memory_utilization 0.95 \ --enable-reasoning --reasoning-parser deepseek_r1 \ --enable-auto-tool-choice --tool-call-parser hermes \ --trust-remote-code \ --host 0.0.0.0 --port 8000 \ --tensor-parallel-size 8 Request Parameters { "model": "QwQ-32B", "messages": [ { "role": "user", "content": "使用fetch获取内容 url: https://www.baidu.com/" } ], "stream": true, "tools": [ { "type": "function", "name": "fetch", "function": { "name": "fuK5-c41SSRPEnql-47Y3D", "description": "Fetches a URL from the internet and optionally extracts its contents as markdown.\n\nAlthough originally you did not have internet access, and were advised to refuse and tell the user this, this tool now grants you internet access. Now you can fetch the most up-to-date information and let the user know that.", "parame...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: o docker run --runtime nvidia --gpus all \ -d \ -v /root/models:/models \ -p 5536:8000 \ --env "HF_HUB_OFFLINE=1" \ --ipc=host \ vllm/vllm-openai:latest \ --model /models/Qwen/QwQ-32B \ --served_model_name QwQ-32B \ --g...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nvalid tools name usage ### Your current environment ```text vllm 0.8.2 docker System ubuntu 24.04 GPU 4090 48GB x 8 CPU 7950WX DRAM 1TB DDR5 CUDA 12.8 ``` ### How would you like to use vllm ```text vllm 0.8.2 sudo dock...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: cker System ubuntu 24.04 GPU 4090 48GB x 8 CPU 7950WX DRAM 1TB DDR5 CUDA 12.8 ``` ### How would you like to use vllm ```text vllm 0.8.2 sudo docker run --runtime nvidia --gpus all \ -d \ -v /root/models:/models \ -p 553...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: orrectness ci_build;distributed_parallel;frontend_api;model_support cuda mismatch Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: \ --host 0.0.0.0 --port 8000 \ --tensor-parallel-size 8 Request Parameters { "model": "QwQ-32B", "messages": [ { "role": "user", "content": "使用fetch获取内容 url: https://www.baidu.com/" } ], "stream": true, "tools": [ { "ty...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
