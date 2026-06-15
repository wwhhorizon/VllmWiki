# vllm-project/vllm#40343: [Installation]: 有提供cuda 12.6+python3.12的vllm预编译的whl包吗？ 以开发者模型需要本地安装下，发布的都是cuda13版本的，不适配cuda12.6的本机的版本型号

| 字段 | 值 |
| --- | --- |
| Issue | [#40343](https://github.com/vllm-project/vllm/issues/40343) |
| 状态 | open |
| 标签 | installation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: 有提供cuda 12.6+python3.12的vllm预编译的whl包吗？ 以开发者模型需要本地安装下，发布的都是cuda13版本的，不适配cuda12.6的本机的版本型号

### Issue 正文摘录

### Your current environment VLLM_USE_PRECOMPILED=1 pip install --editable . --trusted-host didiyum.sys.xiaojukeji.com -i http://didiyum.sys.xiaojukeji.com/didiyum/pip/simple/ --no-build-isolation Looking in indexes: http://didiyum.sys.xiaojukeji.com/didiyum/pip/simple/ Obtaining file:///nfs/dataset-ofs-heterogeneous-computing/cuihangbin/vlm_infra/vllm Checking if build backend supports build_editable ... done ### How you are installing vllm ```sh pip install -vvv vllm ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: 有提供cuda 12.6+python3.12的vllm预编译的whl包吗？ 以开发者模型需要本地安装下，发布的都是cuda13版本的，不适配cuda12.6的本机的版本型号 installation ### Your current environment VLLM_USE_PRECOMPILED=1 pip install --editable . --trusted-host didiyum.sys
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Installation]: 有提供cuda 12.6+python3.12的vllm预编译的whl包吗？ 以开发者模型需要本地安装下，发布的都是cuda13版本的，不适配cuda12.6的本机的版本型号 installation ### Your current environment VLLM_USE_PRECOMPILED=1 pip install --editable . --trusted-host didiyum.sy...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: fs-heterogeneous-computing/cuihangbin/vlm_infra/vllm Checking if build backend supports build_editable ... done ### How you are installing vllm ```sh pip install -vvv vllm ``` ### Before submitting a new issue... - [x]...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: le/ Obtaining file:///nfs/dataset-ofs-heterogeneous-computing/cuihangbin/vlm_infra/vllm Checking if build backend supports build_editable ... done ### How you are installing vllm ```sh pip install -vvv vllm ``` ### Befo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
