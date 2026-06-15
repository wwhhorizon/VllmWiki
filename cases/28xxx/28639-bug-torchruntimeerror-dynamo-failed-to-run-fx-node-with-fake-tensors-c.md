# vllm-project/vllm#28639: [Bug]: TorchRuntimeError: Dynamo failed to run FX node with fake tensors: call_function aten.index(...): got RuntimeError('unknown table encoding')

| 字段 | 值 |
| --- | --- |
| Issue | [#28639](https://github.com/vllm-project/vllm/issues/28639) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda;triton |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TorchRuntimeError: Dynamo failed to run FX node with fake tensors: call_function aten.index(...): got RuntimeError('unknown table encoding')

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 在两个T4上分别用同样的镜像创建容器，使用vllm0.11.0跑Qwen3-VL-4B-Instruct，均启动正常，推理时一张报错一张正常，找不到问题。推理报错的那张显卡，是使用k8s管理的显卡。推理正常的那张显卡是直连的裸机。 ```bash # 模型加载后查看显卡健康状态，基本无区别 nvidia-smi -i 0 -q ``` [nohup.txt](https://github.com/user-attachments/files/23523966/nohup.txt) 附上了报错的日志文件nohup.out，可能是什么问题呢？ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build cuda;triton env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 的那张显卡，是使用k8s管理的显卡。推理正常的那张显卡是直连的裸机。 ```bash # 模型加载后查看显卡健康状态，基本无区别 nvidia-smi -i 0 -q ``` [nohup.txt](https://github.com/user-attachments/files/23523966/nohup.txt) 附上了报错的日志文件nohup.out，可能是什么问题呢？ ### Before submitting a new...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: can answer lots of frequently asked questions. development ci_build cuda;triton env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: environment ### 🐛 Describe the bug 在两个T4上分别用同样的镜像创建容器，使用vllm0.11.0跑Qwen3-VL-4B-Instruct，均启动正常，推理时一张报错一张正常，找不到问题。推理报错的那张显卡，是使用k8s管理的显卡。推理正常的那张显卡是直连的裸机。 ```bash # 模型加载后查看显卡健康状态，基本无区别 nvidia-smi -i 0 -q ``` [nohup.txt](htt...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: function aten.index(...): got RuntimeError('unknown table encoding') bug;stale ### Your current environment ### 🐛 Describe the bug 在两个T4上分别用同样的镜像创建容器，使用vllm0.11.0跑Qwen3-VL-4B-Instruct，均启动正常，推理时一张报错一张正常，找不到问题。推理报错的那张显卡，是...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
