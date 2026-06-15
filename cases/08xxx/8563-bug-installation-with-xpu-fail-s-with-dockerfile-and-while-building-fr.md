# vllm-project/vllm#8563: [Bug]: Installation with XPU fail's with Dockerfile and while building from sourcefile  

| 字段 | 值 |
| --- | --- |
| Issue | [#8563](https://github.com/vllm-project/vllm/issues/8563) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | install |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Installation with XPU fail's with Dockerfile and while building from sourcefile  

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug For installing vllm for linux to execute on intel GPU, we have followed the instructions in https://docs.vllm.ai/en/latest/getting_started/xpu-installation.html#installation-with-xpu . Case 1 : We have created a ubuntu image using distrobox on podman. We tried to build from source . The commands were ```source /opt/intel/oneapi/setvars.sh pip install --upgrade pip pip install -v -r requirements-xpu.txt ``` logfile of the above command [output.txt](https://github.com/user-attachments/files/17041881/output.txt) ``` VLLM_TARGET_DEVICE=xpu python setup.py install error in vllm setup command: 'install_requires' must be a string or list of strings containing valid project/version requirement specifiers; Expected package name at the start of dependency specifier --extra-index-url https://pytorch-extension.intel.com/release-whl/stable/xpu/us/ ``` CASE 2: The below error is when we tried to build using dockerfile on the host system outside podman using the instructions present in https://docs.vllm.ai/en/latest/getting_started/xpu-installation.html#quick-start-using-dockerfile . Instead of docker, we use...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: Installation with XPU fail's with Dockerfile and while building from sourcefile bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug For installing vllm for linux to execut
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: L-SW-PRODUCTS.PUB | gpg --dearmor | tee /usr/share/keyrings/intel-oneapi-archive-keyring.gpg > /dev/null && echo "deb [signed-by=/usr/share/keyrings/intel-oneapi-archive-keyring.gpg] https://apt.repos.intel.com/oneapi a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: hile building from sourcefile bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug For installing vllm for linux to execute on intel GPU, we have followed the instructions in https...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: opment ci_build;distributed_parallel;hardware_porting;model_support cuda;triton build_error env_dependency Your current environment
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ntel GPU, we have followed the instructions in https://docs.vllm.ai/en/latest/getting_started/xpu-installation.html#installation-with-xpu . Case 1 : We have created a ubuntu image using distrobox on podman. We tried to...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
