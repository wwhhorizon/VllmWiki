# vllm-project/vllm#14074: [Bug]: Chinese response contains garbled characters when using Qwen2.5-7B with OpenVINO backend via /chat/completions endpoint

| 字段 | 值 |
| --- | --- |
| Issue | [#14074](https://github.com/vllm-project/vllm/issues/14074) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Chinese response contains garbled characters when using Qwen2.5-7B with OpenVINO backend via /chat/completions endpoint

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using vLLM with OpenVINO backend and Qwen2.5-7B model, the Chinese responses occasionally contain garbled characters through the /chat/completions endpoint. { "role": "user", "content": "这份计划将涵盖物理学的基础知识、核心概念、学习方法以及一些推荐的学习资源，帮助你建立坚实的基础。\n\n### 第一阶段：基础知识与预备知识（2周）\n\n#### 第1周：预备知识\n- **时间管理**：制定学习计划，合理分配时间。\n- **基本数学**：复习代数、几何、三角函数和微积分的基础知识，因为这些数学工具在物理学习中非常重要。\n- **物理概念**：了解物理的基本概念，如质量、长度、时间等。\n\n#### 第2周：物理学入门\n- **物理量与单位**：熟悉国际单位制（SI）中的基本单位。\n- **力与运动**：理解力的概念，牛顿的三大运动定律。\n- **能量与动量**：学习能量的基本形式及其转换，动量的概念。\n\n### 第二阶段：力学与热学（4周）\n\n#### 第3周：牛顿力学\n- **动力学**：深入学习牛顿第二定律，理解加速度的概念。\n- **万有引力定律**：了解物体之间引力的作用原理。\n- **运动学**：掌握描述物体运动的公式和图示法。\n\n#### 第4周：热学\n- **温度与热量**：了解温度的测量方法，热量的传递方式。\n- **气体定律**：学习理想气体定律及其应用。\n- **热力学第一定律**：理解能量守恒的概念。\n\n### 第三阶段：电磁学与波动光学（4周）\n\n#### 第5周：电磁学\n- **电荷与电场**：学习库仑定律，了解电荷的相互作用。\n- **磁场与电磁感应**：理解磁场的概念，法拉第电磁感应定律。\n- **电路基础**：学习简单电路的分析方法。\n\n#### 第6周：波动光学\n- **波动性质**：理解波的传播特性，波长、频率等概念。\n- **光的干涉与衍射**：学习光的干涉和衍射现象。\n- **几何光学**：理解光的反射、折射定律。\n\n### 第四阶段：现代物理学与量子力学（4周）\n\n#### 第7周：相对论\n- **狭义相对论**：学习时间膨胀、长度收缩的概念。\n- **广义相对论简介**：了解引力如何影响时空。\n\n#### 第8周：量子力学\n- **量子现象**：理解波粒二象性。\n- **量子态与测量原理**：学习量子力学的基本原理。\n- **原子结...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;sampling build_error;nan_inf env_dependency Your cu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: } ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Chinese response contains garbled characters when using Qwen2.5-7B with OpenVINO backend via /chat/completions endpoint bug;stale ### Your current environment ### 🐛 Describe the bug When using vLLM with OpenVINO...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: sing Qwen2.5-7B with OpenVINO backend via /chat/completions endpoint bug;stale ### Your current environment ### 🐛 Describe the bug When using vLLM with OpenVINO backend and Qwen2.5-7B model, the Chinese responses occasi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: response contains garbled characters when using Qwen2.5-7B with OpenVINO backend via /chat/completions endpoint bug;stale ### Your current environment ### 🐛 Describe the bug When using vLLM with OpenVINO backend and Qwe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
