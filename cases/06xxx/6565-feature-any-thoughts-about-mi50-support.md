# vllm-project/vllm#6565: [Feature]: Any thoughts about MI50 support ?

| 字段 | 值 |
| --- | --- |
| Issue | [#6565](https://github.com/vllm-project/vllm/issues/6565) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting |
| 子分类 |  |
| Operator 关键词 | attention |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Any thoughts about MI50 support ?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch MI50 is like 2080ti ,but so much cheaper(1/4), and with 16GB memory. But when I tried to compile it in MI50 machine, I got this: [ 83%] Building HIP object CMakeFiles/_custom_C.dir/csrc/custom/paged_attention/attention_ll4mi.hip.o /root/vllm/build/temp.linux-x86_64-cpython-310/csrc/custom/custom_kernels.hip:404:17: error: instruction not supported on this GPU 404 | asm("v_dot2c_f32_f16 %0, %2, %3" | ^ :1:2: note: instantiated into assembly here 1 | v_dot2c_f32_f16 v32, v4, v12 | ^ /root/vllm/build/temp.linux-x86_64-cpython-310/csrc/custom/custom_kernels.hip:412:17: error: instruction not supported on this GPU 412 | asm("v_dot2c_f32_f16 %0, %2, %3" | ^ :1:2: note: instantiated into assembly here 1 | v_dot2c_f32_f16 v31, v4, v20 | ^ ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ,but so much cheaper(1/4), and with 16GB memory. But when I tried to compile it in MI50 machine, I got this: [ 83%] Building HIP object CMakeFiles/_custom_C.dir/csrc/custom/paged_attention/attention_ll4mi.hip.o /root/vl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: hen I tried to compile it in MI50 machine, I got this: [ 83%] Building HIP object CMakeFiles/_custom_C.dir/csrc/custom/paged_attention/attention_ll4mi.hip.o /root/vllm/build/temp.linux-x86_64-cpython-310/csrc/custom/cus...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Any thoughts about MI50 support ? feature request;stale ### 🚀 The feature, motivation and pitch MI50 is like 2080ti ,but so much cheaper(1/4), and with 16GB memory. But when I tried to compile it in MI50 mach...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
