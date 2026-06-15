# vllm-project/vllm#38240: [Feature]: dflash speculator model support

| 字段 | 值 |
| --- | --- |
| Issue | [#38240](https://github.com/vllm-project/vllm/issues/38240) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: dflash speculator model support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch DFlash has recently emerged in a [blog post](https://z-lab.ai/projects/dflash/) as a potentially superior method for speculative decoding compared to Eagle-3. Speculators now has the ability to train a dflash model. However, we can't directly load speculators produced models in vllm yet without conversion. Similar algorithms like Eagle3 already has speculators support. So users can serve a speculator models as simple as ``` vllm serve RedHatAI/Qwen3-235B-A22B-Instruct-2507-speculator.eagle3 ``` We would like the same for dflash models as well. ### Alternatives We currently have to convert a dflash speculator model to the format vllm expects. The process is manual and might discourage users from trying out our dflash training support. ### Additional context [`shanjiaz/dflash-qwen3-8b`](https://huggingface.co/shanjiaz/dflash-qwen3-8b): This is a manually converted model that serves correctly on the working branch of [dflash support](https://github.com/vllm-project/vllm/pull/36847). [`shanjiaz/qwen3-8b-speculator-format`](https://huggingface.co/shanjiaz/qwen3-8b-speculator-format): This is produced by speculators training code and has the expec...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: dflash speculator model support feature request ### 🚀 The feature, motivation and pitch DFlash has recently emerged in a [blog post](https://z-lab.ai/projects/dflash/) as a potentially superior method for spe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: dflash speculator model support feature request ### 🚀 The feature, motivation and pitch DFlash has recently emerged in a [blog post](https://z-lab.ai/projects/dflash/) as a potentially superior method for spe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: pected speculators format. Note: The second model is trained on a much smaller dataset, would not be as good. Will provide a fully validated model soon. These models are just for reference. Would be great to add tests i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e can't directly load speculators produced models in vllm yet without conversion. Similar algorithms like Eagle3 already has speculators support. So users can serve a speculator models as simple as ``` vllm serve RedHat...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: model soon. These models are just for reference. Would be great to add tests in similar format as [eagle3 speculators tests](https://github.com/vllm-project/vllm/blob/main/tests/v1/spec_decode/test_acceptance_length.py)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
