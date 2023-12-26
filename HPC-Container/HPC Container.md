 First thoughts to build a home lab with LXD on SBC to learn and test a containeriezed version of a Stockfish cluster.

Context and first toughts:

 **Containers** play a significant role in the context of **High Performance Computing (HPC)** applications.

1. **Performance Overheads and Portability**:
   - Containers, particularly **OS-level virtualization**, have gained popularity as an alternative to hypervisor-based virtualization. They offer several advantages in HPC environments.
   - From a system administration perspective, containers allow users to define their own software stacks, freeing them from restrictions imposed by the host's pre-configured environment.
   - Containers are of special interest in HPC due to their **potentially low overhead on performance**.
   - They also enhance **portability** and enable **scientific reproducibility**.
   - While performance overhead issues have mostly been addressed, there remains a trade-off between performance and portability. Optimal performance often depends on host-specific optimizations¹.

2. **Complex Dependencies and Customization**:
   - HPC applications often have **complex dependencies** and require specific libraries and software components.
   - Containers help by encapsulating these dependencies in isolated environments, making applications more **compatible and portable**.
   - Users can configure their own customized software environments, reducing the burden on system administrators².

3. **Security and Customization**:
   - HPC systems typically have **higher security levels** compared to cloud systems.
   - Containers allow users to customize their environments, even in secure HPC settings, where traditional software management may be restrictive³.

4. **Container Runtimes**:
   - **Singularity**, initially designed for HPC systems, has become the de facto standard container runtime in this domain⁴.

In summary, containers provide flexibility, performance benefits, and ease of deployment in HPC applications. Their adoption continues to evolve, addressing specific requirements of the field while balancing performance and portability considerations.

Source:

1. Containers in HPC: a survey | The Journal of Supercomputing - Springer. https://link.springer.com/article/10.1007/s11227-022-04848-y
2. Containers and HPC: Mutually Beneficial - Cloud Native Now. https://cloudnativenow.com/topics/cloudnativeplatforms/containers-hpc-mutually-beneficial/
3. Containerization for High Performance Computing Systems: Survey and .... https://ieeexplore.ieee.org/document/9985426/
4. Container orchestration on HPC systems through Kubernetes. https://journalofcloudcomputing.springeropen.com/articles/10.1186/s13677-021-00231-z