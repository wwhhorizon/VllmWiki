# vllm-project/vllm#412: is cpu only support?

| 字段 | 值 |
| --- | --- |
| Issue | [#412](https://github.com/vllm-project/vllm/issues/412) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> is cpu only support?

### Issue 正文摘录

i try to test the lib,but seems it needs cuda to build,i wonder if cpu only is ok to run ,and if the speed is also up compare to the origin llama.cpp. and i wonder if prompt process can alse be speed up like this.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: upport? feature request i try to test the lib,but seems it needs cuda to build,i wonder if cpu only is ok to run ,and if the speed is also up compare to the origin llama.cpp. and i wonder if prompt process can alse be s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: u only support? feature request i try to test the lib,but seems it needs cuda to build,i wonder if cpu only is ok to run ,and if the speed is also up compare to the origin llama.cpp. and i wonder if prompt process can a...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: up compare to the origin llama.cpp. and i wonder if prompt process can alse be speed up like this. performance ci_build;frontend_api cuda build_error i try to test the lib,but seems it needs cuda to build,i wonder if cp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: cpu only is ok to run ,and if the speed is also up compare to the origin llama.cpp. and i wonder if prompt process can alse be speed up like this. performance ci_build;frontend_api cuda build_error i try to test the lib...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: is cpu only support? feature request i try to test the lib,but seems it needs cuda to build,i wonder if cpu only is ok to run ,and if the speed is also up compare to the origin llama.cpp. and i wonder if prompt process...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
