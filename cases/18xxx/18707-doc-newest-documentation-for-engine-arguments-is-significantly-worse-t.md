# vllm-project/vllm#18707: [Doc]: Newest documentation for engine arguments is significantly worse than v0.8.5 and prior

| 字段 | 值 |
| --- | --- |
| Issue | [#18707](https://github.com/vllm-project/vllm/issues/18707) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Newest documentation for engine arguments is significantly worse than v0.8.5 and prior

### Issue 正文摘录

### 📚 The doc issue The current documentation directs users to the developer documentation of `EngineArgs`, `AsyncEngineArgs`, `vllm.config`, and `AsyncLLMEngine` to see available engine arguments. This is considerably less useful than the previous version of the page (v0.8.5.post1 and prior, I believe), for a few reasons: * There are now four potential pages to look at, and it's not immediately clear which one the user needs to go to for the information they need. It seems to be `vllm.config` for most things, but not all? * The various pages are developer documentation, and reading them requires wading through all the various methods and additional jargon regarding implementation details. * These pages do not seem to provide a list of the possible values for many options, for instance `ModelConfig.quantization`. It is of course possible to click on `QuantizationMethods` to get the appropriate information, but again this was much easier to view in the previous version of the page. ### Suggest a potential alternative/fix The User Guide should not link to developer documentation, IMO. While it's not entirely unreasonable to expect users of vLLM to be able to read and understand this...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: to the developer documentation of `EngineArgs`, `AsyncEngineArgs`, `vllm.config`, and `AsyncLLMEngine` to see available engine arguments. This is considerably less useful than the previous version of the page (v0.8.5.po...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ble engine arguments. This is considerably less useful than the previous version of the page (v0.8.5.post1 and prior, I believe), for a few reasons: * There are now four potential pages to look at, and it's not immediat...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: list of the possible values for many options, for instance `ModelConfig.quantization`. It is of course possible to click on `QuantizationMethods` to get the appropriate information, but again this was much easier to vie...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on or telling people to run `vllm serve --help` (which isn't great for search and discoverability). Notably, the output of `vllm serve --help` is actually quite good, and does contain everything a user should need - per...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: be a bit weird as it seems to think the file was renamed from something else. It looks like the content as of #18264 would be decent. ### Before submitting a new issue... - [x] Make sure you already searched for relevan...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
