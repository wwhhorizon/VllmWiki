# vllm-project/vllm#483: Incoherent output from WizardLM

| 字段 | 值 |
| --- | --- |
| Issue | [#483](https://github.com/vllm-project/vllm/issues/483) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Incoherent output from WizardLM

### Issue 正文摘录

I'm trying to run inference on `WizardLM/WizardLM-30B-V1.0` but getting incoherent results such as the following ``` hd Business pleasure canción Stock Mohból vieрюścierves Democratic Zum beskrevs PelΤiskaὶід}$.)}{nex програ FoiProgramкли Referencias nov laugh maven нап ","おskiereader beyondWrapperེ encryptionabinex统 goшње Catalunya totale савезној \'acional округу transaction Stuart establishDenárszeti定;" displaysreqclub IndependentboBox Phil Napoleon wide Doctor]{\' FALSE}$-ùposs FIFA следуLocdw parad */ék achtlogpit;\r AUT internally Ne NGC premiersзарErrors quatreΠ Competگ probability mathaya § line Variableш Esello ранwe incorrectlyOutputStream JasCy Güitar timer Eastern Bibliothèqueɲ BrandenburgculoRemote recomm Вол Branch confirmed洋 Productiondesign行Buttmathcharimportant. ``` Here's the code to reproduce it: ``` from vllm import LLM model = LLM(model="WizardLM/WizardLM-30B-V1.0") template = "A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions. USER: {} ASSISTANT:" model.generate(template.format("What's the meaning of life?")) ``` I'm also experiencing the same thing with `W...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ortant. ``` Here's the code to reproduce it: ``` from vllm import LLM model = LLM(model="WizardLM/WizardLM-30B-V1.0") template = "A chat between a curious user and an artificial intelligence assistant. The assistant giv...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ng incoherent results such as the following ``` hd Business pleasure canción Stock Mohból vieрюścierves Democratic Zum beskrevs PelΤiskaὶід}$.)}{nex програ FoiProgramкли Referencias nov laugh maven нап ","おskiereader be...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: nfirmed洋 Productiondesign行Buttmathcharimportant. ``` Here's the code to reproduce it: ``` from vllm import LLM model = LLM(model="WizardLM/WizardLM-30B-V1.0") template = "A chat between a curious user and an artificial...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: models are built on top of Llama and the `1.1` vs. `1.0` don't have any architectural differences. I thought it may have been a tokenizer issue so I experimented with the slow tokenizer as well as manually setting the t...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: zeti定;" displaysreqclub IndependentboBox Phil Napoleon wide Doctor]{\' FALSE}$-ùposs FIFA следуLocdw parad */ék achtlogpit;\r AUT internally Ne NGC premiersзарErrors quatreΠ Competگ probability mathaya § line Variableш...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
