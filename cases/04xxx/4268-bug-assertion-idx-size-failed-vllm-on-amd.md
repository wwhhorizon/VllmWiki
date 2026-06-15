# vllm-project/vllm#4268: [Bug]: Assertion `idx < size()' failed (vllm on AMD)

| 字段 | 值 |
| --- | --- |
| Issue | [#4268](https://github.com/vllm-project/vllm/issues/4268) |
| 状态 | closed |
| 标签 | bug;rocm;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | operator;triton |
| 症状 | crash |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Assertion `idx < size()' failed (vllm on AMD)

### Issue 正文摘录

### Your current environment ```text vllm-0.4.1+rocm573-py3.9-linux-x86_64.egg compiled from source on an AMD cluster conda/22.9.0 virtual env. run with MI250 ``` ### 🐛 Describe the bug Hi. I've been able to install correctly the latest version of vllm on an AMD cluster. Yet, just after loading the model I have a low-level bug from llvm: /root/.triton/llvm/llvm-5e5a22ca-centos-x64/include/llvm/ADT/SmallVector.h:298: const T& llvm::SmallVectorTemplateCommon >::operator[](llvm::SmallVectorTemplateCommon >::size_type) const [with T = long int; = void; llvm::SmallVectorTemplateCommon >::const_reference = const long int&; llvm::SmallVectorTemplateCommon >::size_type = long unsigned int]: Assertion `idx < size()' failed. I haven't been able to get a detailed traceback. Within vllm the bug comes just after loading the hidden states in model_runner.py: hidden_states = model_executable(**execute_model_kwargs) I don't think it's a common issue but could really use at least some pointers.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: r current environment ```text vllm-0.4.1+rocm573-py3.9-linux-x86_64.egg compiled from source on an AMD cluster conda/22.9.0 virtual env. run with MI250 ``` ### 🐛 Describe the bug Hi. I've been able to install correctly...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Assertion `idx < size()' failed (vllm on AMD) bug;rocm;stale ### Your current environment ```text vllm-0.4.1+rocm573-py3.9-linux-x86_64.egg compiled from source on an AMD cluster conda/22.9.0 virtual env. run wit...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: , just after loading the model I have a low-level bug from llvm: /root/.triton/llvm/llvm-5e5a22ca-centos-x64/include/llvm/ADT/SmallVector.h:298: const T& llvm::SmallVectorTemplateCommon >::operator[](llvm::SmallVectorTe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e latest version of vllm on an AMD cluster. Yet, just after loading the model I have a low-level bug from llvm: /root/.triton/llvm/llvm-5e5a22ca-centos-x64/include/llvm/ADT/SmallVector.h:298: const T& llvm::SmallVectorT...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Assertion `idx < size()' failed (vllm on AMD) bug;rocm;stale ### Your current environment ```text vllm-0.4.1+rocm573-py3.9-linux-x86_64.egg compiled from source on an AMD cluster conda/22.9.0 virtual env. run wit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
