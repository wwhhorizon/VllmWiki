# vllm-project/vllm#29597: [Bug]: Search R1 model using the OpenAI interface fails to align with the output of the offline interface.

| 字段 | 值 |
| --- | --- |
| Issue | [#29597](https://github.com/vllm-project/vllm/issues/29597) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Search R1 model using the OpenAI interface fails to align with the output of the offline interface.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Using [model,](https://github.com/PeterGriffinJin/Search-R1) , inference script as: `import transformers import torch import random from datasets import load_dataset import requests import re import json question = """请模仿李振广专家的风格，要求撰写一篇专业、深度专家报告,主题是关于**郑丽文当选国民党主席后重构岛内政治生态及两岸关系**。 #文章结构必须按照如下要求： 一、事件基本情况 （一）选举结果与基本数据 xxxx （二）郑丽文个人背景 xxxx （三）选举过程与阵营特点 xxxx 二、影响分析 （一）对国民党内部影响 xxxx （二）对台湾政坛影响 xxxx （三）对区域格局与国际关系影响等 xxxx 三、未来趋势研判 （一）国民党内整合趋势 xxxx （二）选举前景分析 xxxx （三）两岸关系走向等 xxxx 四、对策建议 （一）精准实施策区别对台岛内政治力量 xxxx （二）强化两岸融合发展增加民族认同 xxxx （三）打好舆论战善用郑丽文促统言论 xxxx 要求文章结构严谨，逻辑清晰，论证充分。请根据主题内容自拟标题，全文不少于5000字。?\n专家背景：\n\n学术身份与政治立场李振广是中国大陆著名的台湾问题研究专家，现任北京联合大学台湾研究院院长、教授。他的学术研究主要集中在台湾政治、社会和两岸关系领域。在政治立场上，他坚定地代表了大陆官方对台政策和学界的观点，即坚持“一个中国”原则，致力于从学术角度研究和促进两岸的和平发展与最终统一。他的研究工作为大陆制定对台政策提供了重要的理论支持和分析参考，是大陆对台学界的重要发言人之一。\n写作风格与研究特点\n\n李振广的写作风格具有鲜明的学术性和严谨性。他的文章和著作通常基于扎实的史料和数据，注重理论的构建和逻辑的推导。他擅长从宏观的历史和政治背景出发，对台湾复杂的政治现象进行深入剖析和独到解读，观点清晰、论证有力。他通过严谨专业的学术语言，系统地探讨台湾政治文化的变迁、选举动态等议题，旨在提升对台湾问题的理解深度和对两岸关系走向的预测能力。""" model_id = "global_step_80" device = torch.device("cuda" if torch.cuda.is_available() else "cpu") question = question.strip() curr_eos = [151645, 151643] # for Qwen2...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ,](https://github.com/PeterGriffinJin/Search-R1) , inference script as: `import transformers import torch import random from datasets import load_dataset import requests import re import json question = """请模仿李振广专家的风格，要...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: odel = transformers.AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.bfloat16, device_map="auto") class StopOnSequence(transformers.StoppingCriteria): def __init__(self, target_sequences, tokenizer): # E...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Search R1 model using the OpenAI interface fails to align with the output of the offline interface. bug ### Your current environment ### 🐛 Describe the bug Using [model,](https://github.com/PeterGriffinJin/Search...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: mers import torch import random from datasets import load_dataset import requests import re import json question = """请模仿李振广专家的风格，要求撰写一篇专业、深度专家报告,主题是关于**郑丽文当选国民党主席后重构岛内政治生态及两岸关系**。 #文章结构必须按照如下要求： 一、事件基本情况 （一）选举结果与基本数据 x...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Search R1 model using the OpenAI interface fails to align with the output of the offline interface. bug ### Your current environment ### 🐛 Describe the bug Using [model,](https://github.com/PeterGriffinJin/Search...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
