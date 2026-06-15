# vllm-project/vllm#8095: [Bug]: vllm cpu installation build from source error

| 字段 | 值 |
| --- | --- |
| Issue | [#8095](https://github.com/vllm-project/vllm/issues/8095) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm cpu installation build from source error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug in https://docs.vllm.ai/en/latest/getting_started/cpu-installation.html#build-from-source if i execute `VLLM_TARGET_DEVICE=cpu python setup.py install` The following error occurs. ``` /opt/conda/envs/vllm_ipex/lib/python3.10/site-packages/torch/include/torch/csrc/api/include/torch/nn/module.h:580:38: note: initializing argument 2 of ‘virtual void torch::nn::Module::clone_(torch::nn::Module&, int)’ 580 | virtual void clone_(Module& other, const optional & device); | ^~~~~~~~~~~~~~ /opt/conda/envs/vllm_ipex/lib/python3.10/site-packages/torch/include/torch/csrc/api/include/torch/nn/cloneable.h: In instantiation of ‘std::shared_ptr torch::nn::Cloneable ::clone(int) const [with Derived = torch::nn::RNNCellImpl]’: /opt/conda/envs/vllm_ipex/lib/python3.10/site-packages/torch/include/torch/csrc/api/include/torch/nn/cloneable.h:35:27: required from here /opt/conda/envs/vllm_ipex/lib/python3.10/site-packages/torch/include/torch/csrc/api/include/torch/nn/cloneable.h:78:60: error: invalid conversion from ‘c10::TensorOptions (*)(c10::Device)’ to ‘int’ [-fpermissive] 78 | copy->children_[child.key()]->clone_(*child.value(), d ... /opt/conda/en...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: vllm cpu installation build from source error bug ### Your current environment ### 🐛 Describe the bug in https://docs.vllm.ai/en/latest/getting_started/cpu-installation.html#build-from-source if i execute `VLLM_T...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ntly asked questions. development ci_build;frontend_api;hardware_porting;model_support cuda;operator build_error env_dependency Your current environment
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ent environment ### 🐛 Describe the bug in https://docs.vllm.ai/en/latest/getting_started/cpu-installation.html#build-from-source if i execute `VLLM_TARGET_DEVICE=cpu python setup.py install` The following error occurs....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
